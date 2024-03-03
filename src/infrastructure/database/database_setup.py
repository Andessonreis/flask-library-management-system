import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    database_uri = 'sqlite:///' + os.path.join(basedir, 'infrastructure', 'database', 'library.db')
    
    app.config.update(
        SQLALCHEMY_DATABASE_URI=database_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECRET_KEY='secret_key'
    )

    # Cria a instância do SQLAlchemy 
    db = SQLAlchemy(app)

    # Cria um blueprint para usuários
    user_bp = Blueprint('user', __name__)
    # Registra o blueprint
    app.register_blueprint(user_bp, url_prefix='/user')

    return app, db, user_bp

app, db, user_bp = create_app()
