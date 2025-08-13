from pathlib import Path
import json
 
 
def get_stored_user_info(path):
    if path.exists():
        contents = path.read_text()
        user_data = json.loads(contents)
        return user_data
    else:
        return None
 
 
def set_new_user(path):
    username = input('用户名:')
    age = input('年龄:')
    city = input('城市：')
    user_data = {'username': username, 'age': age, 'city': city}
    contents = json.dumps(user_data)
    path.write_text(contents)
    print(f"已经存储{user_data['username']}的信息")
    return user_data
 
 
def greet_user():
    path = Path('user_data.json')
    user_data = get_stored_user_info(path)
    if user_data:
        print(f"欢迎您，{user_data['username']},您的年龄是{user_data['age']}岁，您来自{user_data['city']}城市")
    else:
        user_data = set_new_user(path)
        print(f"记录您的信息{user_data['username']}")
 
 
greet_user()

import math
import numpy as np
import matplotlib.pyplot as plt