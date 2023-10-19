from telegram import User
from src.utils.users import get_username

def log_command(command: str, user: User) -> None:
    print(f'/{command} - {get_username(user)}')