from src.infrastructure.database.sqlalchemy import db
from src.domain.User import User

class UserRepository:
    @staticmethod
    def create_user(name: str, email: str, password: str, is_admin: bool = False) -> User:
        """
        Cria um novo usuário no banco de dados.

        Args:
            name (str): O nome do usuário.
            email (str): O email do usuário.
            password (str): A senha do usuário.
            is_admin (bool, optional): Indica se o usuário é um administrador. Default é False.

        Returns:
            User: O objeto do usuário recém-criado.
        """
        new_user = User(name=name, email=email, password=password, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()
        return new_user
