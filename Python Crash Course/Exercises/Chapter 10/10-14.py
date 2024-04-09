from pathlib import Path
import json

path = Path('userinfo.json')


def get_stored_userinfo(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def greet_user():
    """Greet the user by name."""
    user_info = get_stored_userinfo(path)
    if path.exists():
        confirmation = input(f'Are you {user_info['name']}? y/n ')
    else:
        get_new_user()
        exit
    if confirmation == 'y':
        print(f"Welcome back, {user_info['name']}!")
        print(f"Your username is {user_info['username']}!")
        print(f"Your email is {user_info['email']}!")
    else:
        get_new_user()

def get_new_user():
    name = input("What is your name? ")
    username = input("What is your username? ")
    email = input("What is your email? ")
    user_info = {'name':name,'username':username,'email':email}
    contents = json.dumps(user_info)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {name}!")
    exit

greet_user()
