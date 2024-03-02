from src.infrastructure.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def create_user(name: str, email: str, password: str, is_admin: bool = False) -> User:
        """
        Cria um novo usuário.

        Args:
            name (str): O nome do usuário.
            email (str): O email do usuário.
            password (str): A senha do usuário.
            is_admin (bool, optional): Indica se o usuário é um administrador. Default é False.

        Returns:
            User: O objeto do usuário recém-criado.

        Raises:
            ValueError: Se o email já estiver em uso.
        """
        # Verificar se o email já está em uso
        existing_user = UserRepository.get_user_by_email(email)
        if existing_user:
            raise ValueError("O email já está em uso por outro usuário.")

        # Criar o novo usuário
        new_user = UserRepository.create_user(name, email, password, is_admin)
        return new_user


    @staticmethod
    def create_user(name, email, password):
        existing_user = UserRepository.get_user_by_email(email)
        if existing_user:
            return None, "Email already exists"
        
        new_user = UserRepository.create_user(name, email, password)
        return new_user, None

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def delete_user(user_id):
        return UserRepository.delete_user(user_id)

