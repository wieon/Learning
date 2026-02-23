import json

filename = "056_username.json"

def get_stored_username():
    """如果存储了用户名，就获取它"""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?")
    with open(filename, "w") as f:
        json.dump(username, f)
    return username

def greet_user():
    """欢迎用户"""
    username = get_stored_username()
    if username:
        print("Welcome back, {}!".format(username))
    else:
        username = get_new_username()
        print("Welcome, {}!".format(username))

greet_user()
