from flask_sqlalchemy import SQLAlchemy
from src.infrastructure.database.database_setup import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User(db.Model):
    """Representa um usuário no sistema."""

    __tablename__ = 'users'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    email: str = db.Column(db.String(100), unique=True, nullable=False)
    password_hash: str = db.Column(db.String(100), nullable=False)
    registration_date: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    is_admin: bool = db.Column(db.Boolean, default=False)
    
    def __repr__(self) -> str:
        """Retorna uma representação string do objeto User."""
        return f"<User(id={self.id}, name={self.name}, email={self.email}, is_admin={self.is_admin})>"
        
    def as_dict(self) -> dict:
        """Retorna uma representação em dicionário do objeto User."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'registration_date': self.registration_date.strftime('%Y-%m-%d %H:%M:%S'),
            'is_admin': self.is_admin
        }
