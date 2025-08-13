#for循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:#for循环末尾的冒号告诉Python，下一行是循环的第一行
    print(magician.title()+", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")#没有缩进的代码都只执行一次，而不会重复执行
print("\n")
print("\n")
print("\n")


#测试
pizzas=['haixian','shaoji','niurou']
for pizza in pizzas:
    print('I like '+ pizza.title()+' pizza')
animals=['dog','cat','robbit']
for animal in animals:
    print('A '+animal+' would make a great pet')
print('Any of theseanimals would make a great pet!')
print("\n")
print("\n")
print("\n")


#数值列表
for value in range(1,5):
    print(value)#函数range()让Python从指定的第一个值开始数，并在到达指定的第二个值后停止
numbers = list(range(1,6))#函数list()将range()的结果直接转换为列表
print(numbers)
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
squares = [value**2 for value in range(1,11)]#列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。
print(squares)
print("\n")
print("\n")
print("\n")


#测试
x=[x for x in range(1,21)]
print(x)#数到 20
X2= list(range(1,21))
print(X2)
X3= list(range(1,1000))
print(min(X3))
print(max(X3))
print(sum(X3))
x4=[]
for value in range(1,21,2):
    X4=value
    x4.append(X4)
print(x4)
x4=[x4 for x4 in range(1,21,2)]#range函数的第三个参数是步长（step）,range的用法是range(start, stop, step)
print(x4)
x5=[x5 for x5 in range(3,31,3)]
print(x5)
x6=[]
for X6 in range(1,11):
    XX6=X6**3
    x6.append(XX6)
print(x6)
x6=[X6**3 for X6 in range(1,11)]
print(x6)
print("\n")
print("\n")
print("\n")


#切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])#索引0~3,即输出到第三个
print(players[:4])#没有指定第一个索引时Python将自动从列表开头开始
print(players[-3:])#省略终止索引
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
#复制
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]#同时省略起始索引和终止索引（[:]），创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print("\n")
print("\n")
print("\n")


#测试
x=['apple','orange','banana', 'pear']
print('The first three items in the list are:')
print(x[:3])
pizzas=['haixian','shaoji','niurou']
pizzas.append('xianggu')
friend_foods.append('baicai')
for pizza in pizzas[:]:
    print('My favorite pizzas are:'+ pizza)
for q in friend_foods[:]:
    print('My friends favorite pizzas:'+ q)
print("\n")
print("\n")
print("\n")


#元组
dimensions = (200, 50)#元组使用圆括号，不可变的列表被称为元组
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)#也可以for循环遍历
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)#虽然不能修改元组的元素，但可以给存储元组的变量赋值，即重新定义元组

print("\n")
print("\n")
print("\n")


#测试 自助餐
zizhucan=('鸡','鸭','鹅')
print(zizhucan)
for I in range(3):
    print(zizhucan[I])
zizhucan=('鸡','鸭','鹅')

print(zizhucan)
for I in zizhucan:
    print(I)

print(zizhucan)   
zizhucan=('鸡','s','鹅')
for I in zizhucan:
    print(I)
