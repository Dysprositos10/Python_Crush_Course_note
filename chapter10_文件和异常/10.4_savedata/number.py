#喜欢的数
from pathlib import Path
import json
from pkgutil import get_data
def get_stored_number(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        favor_number = json.loads(contents)
        return favor_number
    else:
        return None

def get_favor_number(path):
    """提示用户输入数字"""
    number = input('please input your favoriate number:')
    contents = json.dumps(number) #json.dumps() 函数生成指定json文件的字符串
    path.write_text(contents) #写入

def number():
    """输出数字"""
    path = Path('favoriate_number.txt') #读取文件
    favor_number = get_stored_number(path)
    if favor_number:
        print(f"I know your favorite number! It's {favor_number}")
    else:
        favor_number = get_favor_number(path)
number()     

print('\n')
#用户字典
from pathlib import Path
import json
def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        user_data = json.loads(contents)
        return user_data
    else:
        return None
def get_new_username(path):
    """提示用户输入用户名"""
    user= input("What is your name? ")
    age = input("How old are your? ")
    city = input("where come form? ")
    user_data = {'user':user,'age':age,'city':city}
    contents = json.dumps(user_data)
    path.write_text(contents)
    return user_data
def greet_user():
    """问候用户，并指出其名字"""
    path = Path('userdata.json')
    user_data = get_stored_username(path)#get_stored_username()获取已存储的用户名
    if user_data:
        Validate_user = input('please last user:')
        if Validate_user == user_data['user']:
            print(f"welcome,{user_data['user']},you are {user_data['age']},you come from {user_data['city']}")
        else:
            print('Please re-enter the user!')
            user_data = get_new_username(path)
            print(f"We'll remember you when you come back, {user_data['user']}!")
    else:
        user_data = get_new_username(path)#否则，get_new_username()输入用户名
        print(f"We'll remember you when you come back, {user_data}!")

greet_user()