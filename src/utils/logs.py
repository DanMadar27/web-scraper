from telegram import User
from datetime import datetime
from src.utils.users import get_username

def log_command(command: str, user: User) -> None:
    print(f'{datetime.now()}: /{command} - {get_username(user)}')