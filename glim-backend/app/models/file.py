from flask import Flask, current_app

# Importações necessárias
from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import json
import librosa
import soundfile as sf
import numpy as np
import moviepy.editor as mp
from pydub import AudioSegment
from pdfminer.high_level import extract_text
import spacy
from spacy import displacy
from spacy.matcher import Matcher
from spacy.tokens import Span
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
from translate import Translator

# Downloads necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

class File:
    
    def __init__(self, app: Flask):
        self.app = app

    def test():
        print(current_app.config)
        return False

    def extrair_audio(self, video_path, filename="audio"):
        video_clip = mp.VideoFileClip(video_path)
        audio_clip = video_clip.audio
        # audio_clip.nchannels = 1
        audio_clip.write_audiofile(f"{current_app.config['UPLOAD_FOLDER_AUDIO']}{filename}.wav")
        self.convert_audio_mono(f"{current_app.config['UPLOAD_FOLDER_AUDIO']}{filename}.wav", filename)


    def convert_audio_mono(audio_path, filename="audio"):
        sound = AudioSegment.from_wav(audio_path)
        sound = sound.set_channels(1)
        output_audio_path = f"{current_app.config['UPLOAD_FOLDER_AUDIO']}{filename}-movo.wav"
        sound.export(output_audio_path, format="wav")

    def transcript_file(audio_path, filaname):
        wf = wave.open(audio_path, 'rb')
        if wf.getnchannels() != 1:
            print('o arquivo de audio deve estar no formato WAV mono PCM')
            exit(1)
            
        model = Model('model')
        rec = KaldiRecognizer(model, wf.getframerate())
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                print(res['text'])
        res = json.loads(rec.FinalResult())
        print(res['text'])
        return False

    def create_patterns(self, pln, novos_padroes):
        matcher = Matcher(pln.vocab)
        # Transforma as novas frases em padrões
        for padrao in novos_padroes:
            tokens = padrao.lower().split()
            pattern = [{"LOWER": token} for token in tokens]
            matcher.add("MEMORY_REFERENCE", [pattern])
            
        return matcher
    
    def process_paragraph(self, texto, pln, matcher):
        # Divide o texto em parágrafos
        paragrafos = texto.split('\n')

        resultado = []

        # Processa cada parágrafo separadamente
        for paragrafo in paragrafos:
            doc = pln(paragrafo)
            matches = matcher(doc)
            if matches:
                spans = []
                
                for match_id, start, end in matches:
                    span = Span(doc, start, end, label="MEMORY_REFERENCE")
                    spans.append(span)
                
                # Atribui as spans diretamente a doc.ents
                doc.ents = spans
                
                highlighted_text = displacy.render(doc, style="ent", jupyter=False)
                highlighted_text = highlighted_text.replace('\n', ' ')
                resultado.append({
                    "paragrafo": paragrafo,
                    "highlighted_text": highlighted_text
                })

        return resultado

    def upload_file(self, file_path, patterns):
        print("Escolha um arquivo em PDF para realizar a busca pelo tipo de memória desejado")
         # Implementação do método
        print(f"Processando arquivo: {file_path}")
        print(f"Padrões: {patterns}")
        
        # Lógica para processar o arquivo
    
        # Verifique se o arquivo existe
        print(file_path)
        if not os.path.exists(file_path):
            print("Arquivo não encontrado.")
            return
            
        # Extrair texto do arquivo PDF
        try:
            pln = spacy.load('pt_core_news_sm')
            
            texto = extract_text(file_path)
            print("Texto extraído com sucesso:")
            print(texto[:500])  # Mostra os primeiros 500 caracteres do texto
            
            matcher = self.create_patterns(pln, patterns)
            
            print("As entidades foram destacadas e salvas no arquivo entities.html")
            return self.process_paragraph(texto, pln, matcher)
        except Exception as e:
            print(f"Erro ao extrair texto: {e}")

    def upload_text(self, text, patterns):
        print("Recebe o texto transcrito.")
        
        # Verifique se o texto existe
        if text == "":
            print("Texto não encontrado.")
            return
            
        # Extrair texto do arquivo PDF
        try:
            pln = spacy.load('pt_core_news_sm')
            
            print("Texto extraído com sucesso:")
            print(text[:500])  # Mostra os primeiros 500 caracteres do texto
            
            matcher = self.create_patterns(pln, patterns)
            
            print("As entidades foram destacadas e salvas no arquivo entities.html")
            return self.process_paragraph(text, pln, matcher)
        except Exception as e:
            print(f"Erro ao extrair texto: {e}")