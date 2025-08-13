#加法计算器
while True:
    number1 = input('Please input number1:')
    if number1 == 'q':
        break
    number2 = input('Please input number2:')
    if number2 == 'q':
        break
    try:
        print(int(number1)+int(number2))
    except ValueError :
        print("You must input int!")

#阅读
from pathlib import Path
pai = Path('pi_digits.txt')
print(pai.read_text())
cat = Path('cat.txt')
try:
    print(cat.read_text())
except FileNotFoundError:
    pass

#阅读2
from pathlib import Path

def count_words(python):
    try:
        content = python.read_text() #调用read_text()访问文件时要先储存量
        print(content)
    except FileNotFoundError:
        print("You must input int!")
    else:
        print("出现次数:",content.count('Python')) #方法count()来确定特定的单词或短语在字符串中出现了多少次

python = Path('learning_python.txt') #在结尾加载函数
count_words(python)

#阅读2:优化
from pathlib import Path

def count_words(file_path):
    try:
        content = file_path.read_text()  # 保存读取内容到变量
        print(content)
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在")
    except Exception as e:
        print(f"读取错误: {e}")
    else:
        print("出现次数:", content.count('Python'))  # 对文本内容进行统计

python_file = Path('learning_python.txt')
count_words(python_file)