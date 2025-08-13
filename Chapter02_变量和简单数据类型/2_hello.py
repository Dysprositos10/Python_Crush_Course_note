name = "ada lovelace"
print(name.title()) #在name.title()中，name后面的句点（.）让Python对变量name执行方法title()指定的操作：首字母大写。

name = "Ada Lovelace" 
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name #""表示空格 ，加号表示空格
print(full_name)

print("Languages:\n\tPython\n\tC\n\tJavaScript") #\t是制表符，\n是换行符

favorite_language = ' python '
favorite_language.rstrip()#rstrip剔除字符串末尾空白，
favorite_language.lstrip()#lstrip剔除字符串开头空白
favorite_language.strip() #strip剔除字符串两端空白

x=("Hello Eric, would you like to learn some Python today?")
print(x)
x=print('Albert Einstein once said, "A person who never made a mistake never tried anything new"')
print((2 + 3) * 4)
print(0.2+0.2)

age = 23
message = "Happy " + str(age) + "rd Birthday!" #函数str()，它让Python将非字符串值表示为字符串
print(message)

print('\n')
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"# f字符串。f是 format（设置格式）的简写,通过把花括号内的变量替换为其值来设置字符串的格式
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)