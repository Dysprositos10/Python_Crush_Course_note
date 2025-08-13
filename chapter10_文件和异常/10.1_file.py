from pathlib import Path #pathlib 模块在各种操作系统中处理文件和目录。提供特定功能的模块通常称为库（library）

path = Path('pi_digits.txt')#Path 对象指向一个文件,例如，这里创建了一个表示文件 pi_digits.txt 的 Path 对象，并将其赋给了变量 path
contents = path.read_text().rstrip()#read_text()方法将该文件的全部内容作为一个字符串返回，而我们将这个字符串赋给了变量 contents
#rstrip()可以删除字符串末尾的空白（空字符串会被视为空行）；连续的方法称为方法链式调用
print(contents) #同一个目录下，知道文件名即可访问

print('\n')
path2 = Path('8.3_import/filename.txt') #相对文件路径让 Python 到相对于当前运行的程序所在目录的指定位置去查找
contents2 = path2.read_text()
print(contents2)

print('\n')
#访问文件中的各行
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text() #处理文件中的各行，无须在读取文件时删除任何空白

lines = contents.splitlines() #splitlines()方法返回一个列表，包含文件中所有的行，并将这个列表赋给了变量 lines
for line in lines:
    print(line) #没有修改这些行，因此输出与原始文件完全一致。

print('\n')
#访问文件中的各行
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
        pi_string += line.lstrip()#lstrip剔除字符串开头空白

print(pi_string)
print(len(pi_string))
#读取文件时会转换为字符串
#要将其作为数值使用时，就必须使用 int() 函数将其转换为整数，或者使用 float() 函数将其转换为浮点数

print('\n')
#访问文件中的各行2
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
        pi_string += line.lstrip()#lstrip剔除字符串开头空白

print(f"{pi_string[:12]}...")#算上小数点的12个字符+...
print(len(pi_string))


print('\n')
#访问文件中的各行3
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()


print('\n')
#测试：访问
from pathlib import Path

path_python = Path('learning_python.txt')
content_python = path_python.read_text()
print(content_python)

print(content_python.splitlines())#返回一个列表,无需临时变量
for i in content_python.splitlines():
    print(i.replace('Python', 'C'))#replace()、strip() 等不会修改原字符串，而是返回一个新字符串。
    #i.replace('Python', 'C')可以后继，无需临时变量

print('\n')
#1 处理 ZeroDivisionError异常
try:#检验代码有无问题，没有则跳过except
    print(5/0)
except ZeroDivisionError:#跳过traceback
    print("You can't divide by zero!")

print('\n')
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:#依赖 try 代码块成功执行的代码都被放在 else 代码块中
          answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
          print("You can't divide by 0!")
    else:
          print(answer)

print('\n')
#2 处理FileNotFoundError异常
from pathlib import Path

path = Path('learning_python.txt')
try:
    contents = path.read_text(encoding='utf-8') #如果要读取的文件不是在系统中创建的，需要encoding让编码一致
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
      #计算文件大致包含多少个单词
    words = contents.split() #split() 方法默认以空白为分隔符将字符串分拆成多个部分
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

print('\n')
#多个文件处理
from pathlib import Path
def count_words(path):
    """计算一个文件大致包含多少个单词"""
    try:
        contents = path.read_text(encoding='utf-8') #如果要读取的文件不是在系统中创建的，需要encoding让编码一致
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
          #计算文件大致包含多少个单词
        words = contents.split() #split()方法默认以空白为分隔符将字符串分拆成多个部分
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
filenames = ['alice.txt', 'learning_python.txt']
for filename in filenames:
    path = Path(filename)#filename当于__init__的对象；也等同于path = Path('learning_python.txt')
    count_words(path)

print('\n')
#多个文件——静默失败
from pathlib import Path
def count_words(path):
    """计算一个文件大致包含多少个单词"""
    try:
        contents = path.read_text(encoding='utf-8') #如果要读取的文件不是在系统中创建的，需要encoding让编码一致
    except FileNotFoundError:
        pass #pass语句在出现异常时，什么都不会发生，还充当了占位符，提醒你在程序的某个地方什么都没有做。
    else:
          #计算文件大致包含多少个单词
        words = contents.split() #split()方法默认以空白为分隔符将字符串分拆成多个部分
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
filenames = ['alice.txt', 'learning_python.txt']
for filename in filenames:
    path = Path(filename)#filename当于__init__的对象；也等同于path = Path('learning_python.txt')
    count_words(path)