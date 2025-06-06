import os
from flask import Blueprint, request, current_app, jsonify
from flask_cors import CORS
from app.models.file import File
from app.models.db import Database

main_bp = Blueprint('main_bp', __name__)
db = Database(main_bp)

CORS(main_bp)

@main_bp.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

@main_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    print("Username: ", username)
    print("Password: ", password)
    
    if username and password:
        return "Login Successful"
    else:
        return "Invalid username or password. Please try again."

@main_bp.route('/users', methods=['GET'])
def listaUsuarios():
    results = db.getUsers()
    if not results:
        return jsonify({"error": "Não foi possível recuperar os usuários"}), 500
    return jsonify(results)

@main_bp.route('/users/<int:user_id>', methods=['GET'])
def pegaUsuario(user_id):
    result = db.getUserById(user_id)
    if not result:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify(result)

@main_bp.route('/users', methods=['POST'])
def cadastraUsuario():
    data = request.json 
    if not data:
        return jsonify({"error": "Dados do usuário não fornecidos"}), 400
    
    if db.addUser(data):
        return jsonify({"message": "Usuário adicionado com sucesso"}), 201
    else:
        return jsonify({"error": "Erro ao adicionar usuário"}), 500

@main_bp.route('/users/<int:user_id>', methods=['PUT', 'PATCH'])
def atualizaUsuario(user_id):
    data = request.json
    if not data:
        return jsonify({"error": "Dados do usuário não fornecidos"}), 400
    
    if db.updateUser(user_id, data):
        return jsonify({"message": f"Dados do usuário ID {user_id} atualizados com sucesso"}), 200
    else:
        return jsonify({"error": f"Erro ao atualizar dados do usuário ID {user_id}"}), 500

@main_bp.route('/users/<int:user_id>', methods=['DELETE'])
def deletaUsuario(user_id):
    if db.deleteUser(user_id):
        return jsonify({"message": f"Usuário ID {user_id} excluído com sucesso"}), 200
    else:
        return jsonify({"error": f"Erro ao excluir usuário ID {user_id}"}), 500

@main_bp.route('/memoria', methods=['POST'])
def memoria():
    print("Chegou aqui")
    print(request.form)
    print(request.files)
    
    # Cria uma instância da classe File
    file_processor = File(current_app)
    
    if 'file' not in request.files:
        return "File not found in request."
    
    file = request.files['file']
    if file.filename == '':
        return "No file selected."
    
    if request.form.get('tags') == '':
        return "No tags selected."
    
    tags = request.form.get('tags')
    patterns = tags.split(',') if tags else []
    
    if file:
        filename = file.filename
    
        fileType = request.form.get('fileType')
        if fileType == ".pdf":
            print("pdf")
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER_PDF'], filename)
            file.save(file_path)
            print(file_path)
                       
            # Chama o método upload_file a partir da instância
            result = file_processor.upload_file(file_path, patterns)
            # return f'Arquivo {filename} carregado com sucesso. Caminho: {file_path}. Transcrição: {result}'
            return jsonify({"message": f'Arquivo {filename} carregado com sucesso. Caminho: {file_path}', "data": result }), 200
        
        else:
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER_VIDEO'], filename)
            file.save(file_path)
            audio_path = f"{current_app.config['UPLOAD_FOLDER_AUDIO']}audio.wav"
            
            # Chama os métodos a partir da instância
            file_processor.extrair_audio(file_path)
            texto = file_processor.transcript_file(audio_path)
            return f'Arquivo {filename} carregado com sucesso. Caminho: {file_path}. Transcrição: {texto}' 
    
    return jsonify({"message": "File not uploaded."}), 500