current_number = 1
while current_number <= 5:#while循环不断地运行，直到指定的条件不满足为止
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""  #空字符串是一个初始值，可以在首次while循环时，与quit比较
while message != 'q':#惊叹号和等号（!=），其中的惊叹号表示不
    message = input(prompt)
    if message!='q':
        print(message)#打印信息后，回到while，再比较是不是quit，不是的话打印prompt


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True #False导致while循环不再继续执行 
while active:
    message = input(prompt)
    if message == 'q':
        active = False
else:
    print(message)


prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break #while True打头的循环将不断运行，直到遇到break语句。(不再运行循环中余下的代码，也不管条件测试的结果如何)
    else:
        print("I'd love to go to " + city.title() + "!")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: #如果当前的数字不能被2整除，就执行循环中余下的代码，Python将这个数字打印出来
        continue #如果结果为0（意味着current_number可被2整除），就执行continue语句，让Python忽略余下的代码，并返回到循环的开头
    print(current_number)