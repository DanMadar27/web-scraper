from telegram import User

def getUsername(user: User) -> str:
    if user.username:
        return user.username
    
    return user.first_name + ' ' + user.last_name + ' (' + str(user.id) + ')'