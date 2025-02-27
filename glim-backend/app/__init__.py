from flask import Flask
import os
from app.config import Config

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    # Verifica se as pastas de upload existem, se não, cria elas
    os.makedirs(app.config['UPLOAD_FOLDER_VIDEO'], exist_ok=True)
    os.makedirs(app.config['UPLOAD_FOLDER_AUDIO'], exist_ok=True)
    os.makedirs(app.config['UPLOAD_FOLDER_PDF'], exist_ok=True)
    
    with app.app_context():
        from app.routes.main import main_bp
        app.register_blueprint(main_bp)
        
    return app
