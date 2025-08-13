#写入一行
from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming.") #write_text()将数据写入该文件

#写入多行
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"#运算符 += 在该变量中追加这个字符串。
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)#如果指定的文件已存在， write_text() 将删除其内容，并将指定的内容写入其中。

#访客簿
from pathlib import Path
name_path = Path('guest_book.txt')  # 在循环外创建Path对象
while True:
    names = input("Please input your name (enter 'q' to quit): ")#输入结果要有变量保存

    if names == 'q':
        break
# 使用追加模式写入并添加换行符
    with name_path.open('a') as file:  # 'a' 表示追加模式；'a' = append mode；将返回结果（文件对象）赋值给 as 后的变量 file
        file.write(f"{names}\n")       # 自动添加换行符


#使用 json.dumps() 和 json.loads()
from pathlib import Path
import json #模块 json能让Python 数据结构转换为 JSON 格式的字符串（通用格式）

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)#json.dumps() 函数生成指定json文件的字符串
path.write_text(contents)

from pathlib import Path
import json

path = Path('numbers.json')#确保读取的是前面写入的文件
contents = path.read_text()#read_text() 方法来读取它
numbers = json.loads(contents)#json.loads()将一个 JSON 格式的字符串作为参数，并返回一个 Python 对象

print(numbers)

#保存数据2
from pathlib import Path
import json

path = Path('username.json')
if path.exists():#如果指定文件存在，exists() 方法返回 True
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:#如果指定文件不存在，返回 Flase，需要输入
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")

#重构
print('\n')
from pathlib import Path
import json
def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
def get_new_username(path):
    """提示用户输入用户名"""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
def greet_user():
    """问候用户，并指出其名字"""
    path = Path('username.json')
    username = get_stored_username(path)#get_stored_username()获取已存储的用户名
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)#否则，get_new_username()输入用户名
        print(f"We'll remember you when you come back, {username}!")
greet_user()