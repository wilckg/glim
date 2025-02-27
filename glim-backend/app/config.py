# import os
# from dotenv import load_dotenv
# load_dotenv()

class Config:
    UPLOAD_FOLDER_VIDEO="/tmp/audio/" #os.environ.get('PATH_VIDEO')
    UPLOAD_FOLDER_AUDIO="/tmp/video/" #os.environ.get('PATH_AUDIO')
    UPLOAD_FOLDER_PDF="/tmp/pdf/"
    MYSQL_HOST="localhost" #os.environ.get('DB_HOST')
    MYSQL_USER="root" #os.environ.get('DB_USER')
    MYSQL_PASSWORD="Gomes#1234" #os.environ.get('DB_PASSWORD')
    MYSQL_DB="memori" #os.environ.get('DB_NAME')
    MYSQL_CURSORCLASS = 'DictCursor'