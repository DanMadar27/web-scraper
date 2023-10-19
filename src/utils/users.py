from telegram import User

def get_username(user: User) -> str:
    if user.username:
        return user.username
    
    return user.first_name + ' ' + user.last_name