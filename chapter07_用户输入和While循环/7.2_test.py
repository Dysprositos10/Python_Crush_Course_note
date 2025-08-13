#披萨配料
prompt = "\n你需要在披萨上添加什么: "
prompt += "\n输入q退出程序"
add=''
while add != 'q':
    add = input(prompt)
    if add != 'q':
        print('我们会在披萨中添加'+ add)

#电影票票价
message = "\n请输入年龄,当输入quit时退出: "
age=''
while age != 'q':
    age = input(message)
    if age != 'q': #年龄不能与q作比较，所以在比较年龄前，要先设定条件：在年龄等于q的情况下重新进入while，比较后终止循环
        if int(age) < 3:
            print('免费')
        elif 3<= int(age) <=12:
            print('10美元')
        else:
            print('15美元')


message = "\n请输入年龄,当输入quit时退出: "
age=''
active = True
while active:
    age = input(message)
    if age == 'q': 
        active = False
    else:
        if int(age) < 3:
            print('免费')
        elif 3<= int(age) <=12:
            print('10美元')
        else:
            print('15美元')

message = "\n请输入年龄,当输入quit时退出: "
age=''
while True:
    age = input(message)
    if age == 'q': 
        break
    else:
        if int(age) < 3:
            print('免费')
        elif 3<= int(age) <=12:
            print('10美元')
        else:
            print('15美元')