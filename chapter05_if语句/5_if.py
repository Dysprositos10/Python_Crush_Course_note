#条件测试
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':#==指变量car的值是'bmw'吗
        print(car.upper())#upper()用于将字符串中的小写字母转换为大写字母，返回新字符串且不修改原字符串
    else:
        print(car.title())


car = 'bmw'
print(car == 'bmw')
car = 'Audi'
print(car == 'audi')#在Python中检查是否相等时区分大小写
car = 'Audi'
print(car.lower() == 'audi')#该测试不区分大小写,函数lower()不会修改存储在变量car中的值


print("\n")
print("\n")
print("\n")
#检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':#惊叹号和等号（!=），其中的惊叹号表示不
    print("Hold the anchovies!")
answer = 17
if answer != 42:
   print("That is not the correct answer. Please try again!")
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)#and or检查多个条件


print("\n")
print("\n")
print("\n")
#检查特定值是否包含/不包含在电脑中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x == y)  # 输出: True
print(x is y)   # 输出: False，is 运算符用于检查两个对象是否是同一个对象，如果两个对象不是同一个对象，即使它们的内容相同，也返回 False。（内存地址不同）
print(x is z)  # 输出: True


print("\n")
print("\n")
print("\n")
#if语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:#只要不满足任何if或elif中的条件测试，其中的代码就会执行
    price = 5
print("Your admission cost is $" + str(price) + ".")


#多个条件，一系列独立的if语句
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")


print("\n")
print("\n")
print("\n")
#测试，外星人颜色
alien_color = 'yellow'
if alien_color == 'green':
    print('The player obtained 5 points')
elif alien_color == 'yellow':
    print('The player obtained 10 points')
else:
    print('The player obtained 15 points')


print("\n")
print("\n")
print("\n")
#测试，人生阶段
age = 66
if age in range(2,5):
    print('幼儿')
elif age in range(4,14):
    print('儿童')
elif age in range(13,21):
    print('青少年')
elif age in range(20,66):
    print('成年人')
else:
    print('老年人')

print("\n")
age = 3
if age < 2:
    print('婴儿')
elif 2<=age<4:
    print('幼儿')
elif age in range(13,21):
    print('青少年')
elif age in range(20,66):
    print('成年人')
elif age > 65:
    print('老年人')

print("\n")   
print("\n") 
print("\n") 
#检查特殊元素
requested_toppings = ['mushrooms','green peppers', 'extra cheese']#列表表示顾客要点的料
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
print("\n")
#确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:#前者遍历列表，下一行print出列表要添加的料
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


print("\n")   
print("\n") 
print("\n")
print("\n") 
print("\n") #上述结合
requested_toppings = ['mushrooms','green peppers', 'extra cheese']#列表表示顾客要点的料
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print("Adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")
print("\nFinished making your pizza!")


print("\n")
print("\n") 
print("\n")
 #使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\n")
print("\n") 
print("\n")
 #测试 用户名
users=['admin','john','amn','s','yowe']
if users:
    for x in users:
        if x == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello '+ x +' thank you for logging in again')
else:
    print('We need to find some users!')

print("\n") 
print("\n") 
print("\n") 
current_users=['Admin','JoHn','amn','s','yowe']
new_users=['Admin','john','dufu','libai']
current_users_lower = [current_user.lower() for current_user in current_users] #遍历现有用户名后，再转换为全小写，在current_users_lower的列表中
for new_user in new_users:    
    if new_user.lower() in current_users_lower: #用new_user的小写去和current_users_lower新列表中的小写比对
        print( new_user +', you need to change your name')
    else:
        print( new_user +', OK')

#if x in current_users or x.lower(): 相当于如果x在x的小写，也要换名字，包含了所有的x

print("\n") 
current_users = ['admin','may','lily','lucy','lisa']
new_users = ['march','april','may','ADMIN','lucy']
for new_user in new_users:
     if new_user in current_users or new_user.lower() in [current_user.lower() for current_user in current_users]:
    #new_user的小写比对current_user的小写
          print(f"\n{ new_user}, you need to change your name.")
     else:
          print(f"\n{ new_user} ,The username is not used,")

print("\n") 
X=[i for i in range(1,10)]
print(X)
for x in X:
    if x == 1:
       print('1st')
    elif x == 2:
       print('2nd')
    elif x == 3:
       print('3rd')
    else:
        print(str(x)+'th') #函数str()，它让Python将非字符串值表示为字符串,整数不能和字符串使用+输出