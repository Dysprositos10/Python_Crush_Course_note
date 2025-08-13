#传递列表
def greet_users(names):#将greet_users()定义成接受一个名字列表的函数
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

print('\n')
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
#模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)
# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


print('\n')
#改写成函数的代码：
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后,都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
# 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models) # 调用print_models()并向它传递两个列表
#切片表示法[:]创建列表的副本：使用的是列表unprinted_designs的副本，而不是列表unprinted_designs本身——函数所做的修改不会影响到列表
show_completed_models(completed_models) #最后引用函数时，输入函数的形参；调用show_completed_models()，并将打印好的模型列表传递给它
print(unprinted_designs)

print('\n')
#测试：魔术师
def show_magicians(unprinted_names,completed_names):
    while unprinted_names:
        print_name=unprinted_names.pop()
        print('Hello, Mr.'+print_name)
        completed_names.append(print_name)
unprinted_names=['Ming','Tian','knight']
completed_names=[]
show_magicians(unprinted_names,completed_names) 
def make_great(unprinted_names,completed_names):
    while unprinted_names:
        print_name=unprinted_names.pop()
        X='The Great '+print_name
        completed_names.append(X)
    print(completed_names)
unprinted_names=['Ming','Tian','knight']
completed_names=[]
make_great(unprinted_names[:],completed_names)
print(unprinted_names)

print('\n')#另一种写法
unprinted_names=['Ming','Tian','knight']
completed_names=[]
def show_magicians(unprinted_names):
    for unprinted_name in unprinted_names:
        print(unprinted_name)
def make_great(unprinted_names,completed_names):
    """在列表中添加the Great字样"""
    for unprinted_name in unprinted_names:
        introduction2 = 'the Great '+ unprinted_name
        completed_names.append(introduction2)
    return completed_names
show_magicians(unprinted_names)
make_great(unprinted_names,completed_names)
show_magicians(completed_names)#make_great函数的结果返回到新列表，但还需要show_magicians整个函数将其打印出来名字

print('\n')
print('\n')
print('\n')
#传递任意数量的实参
def make_pizza(*toppings):#形参名中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都装到这个元组中
    """概述要制作的比萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print('\n')
#位置实参和数量实参
def make_pizza(size, *toppings):#不同类型的实参要放在任意数量实参之前：size
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
    "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')
#使用任意数量的关键字实参
def build_profile(first, last, **user_info):#形参**user_info中的两个星号让Python创建一个名为user_info的空字典
#整个user_info空字典会接受输入键值对
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last #将名和姓加入到profile这个字典中
    for key, value in user_info.items(): #遍历字典user_info中的键—值对;方法items(),它返回一个键—值对列表
        profile[key] = value #将每个键—值对都加入到字典profile中
    return profile #返回值，跳过了每一次的for循环
user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')#将返回的profile存储在变量user_profile中（返回值需要引用,通过print才能输出）
print(user_profile)

print('\n')
#三明治
def sandwichs(*sandwichs):
    """打印顾客点的所有三明治"""
    for sandwich in sandwichs:
        print('Making a '+ sandwich +' sandwich')#sandwichs是元组，必须要for遍历才能加和str
sandwichs('fish','egg','banana')

print('\n')
#汽车
def make_car(Manufacturer_info,model_info,**user_info):
    car={}
    car['Manufacturer'] = Manufacturer_info
    car['model'] = model_info
    for key,value in user_info.items():#方法items(),它返回一个键—值对列表
        car[key] = value
    return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)