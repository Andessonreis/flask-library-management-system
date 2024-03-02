from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Cria a instância do Flask
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
