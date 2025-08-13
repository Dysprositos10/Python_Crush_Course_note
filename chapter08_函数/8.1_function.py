def greet_user(username):#def定义一个函数,冒号后阐述功能
    """显示简单的问候语"""  #文档字符串（docstring）的注释，描述了函数是做什么的，用三引号括起
    print("Hello," + username.title() + "!")
greet_user('jesse')#在greet_user('jesse')中，将实参'jesse'传递给了函数greet_user()，这个值被存储在形参username中。

#测试：消息
def display_message(study):
    print('I study '+ study)
display_message('def')
#测试：喜欢的图书
def favorite_book(title):
    print('One of my favorite books is '+title)
favorite_book('Alice in Wonderland')


print('\n')
#传递实参——位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')#实参'hamster'存储在形参animal_type中，而实参'harry'存储在形参pet_name中
describe_pet('dog', 'willie')#可以多次调用


print('\n')
#传递实参——关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='harry', animal_type='hamster')#关键字实参的顺序无关紧要，因为Python知道各个值该存储到哪个形参中

print('\n')
#传递实参——默认值
def describe_pet(pet_name, animal_type='dog'):#添加了animal_type的默认值dog ; 要注意，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('willie')#只需提供另一个实参
describe_pet(pet_name='harry', animal_type='hamster')#显式地给animal_type提供了实参，Python则忽略这个形参的默认值

print('\n')
#测试：T恤
def make_shirt(shirt_size='L', shirt_message='I love Python'):
    print("The size of the T-shirt is "+shirt_size)
    print("The words are "+shirt_message)
make_shirt()
make_shirt(shirt_message='nobody',shirt_size='M')

print('\n')
#测试：city
def describe_city(city_name='Chongqing',city_country='China'):
    print(city_name+' is in '+city_country)
describe_city()
describe_city('Reykjavik','Iceland')

print('\n')
#返回值——可选实参
def get_formatted_name(first_name,last_name,middle_name=''):#先列出没有默认值的形参
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name #Python将非空字符串解读为True，因此如果函数调用中提供了中间名，if middle_name将为True
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'lee','hendrix') #调用返回值的函数时，需要提供一个变量，用于存储返回的值。
print(musician)

print('\n')
#返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name} #函数build_person()接受名和姓，并将这些值封装到字典中
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age #如果函数调用中包含这个形参的值，这个值将存储到字典中。
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print('\n')
#结合使用函数和 while 循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True: # 这是一个无限循环!
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!") #不能顶格，不然会最后再输出一次print

print('\n')
#城市名
def city_country(city_name,country_name):
    print(city_name.title()+','+country_name.title())
city_country('Beijing','china')
city_country('shanghai','china')
city_country('shenyang','china')

print('\n')
#专辑
def make_album(singer_name,singer_album,number_song=''):
    albums={'name':singer_name,'album':singer_album}
    if number_song:
        albums['number_song'] = number_song
    return albums
album1 = make_album("Taylor Swift", "1989",25)
album2 = make_album("Ed Sheeran", "Divide", 27)
album3 = make_album("Beyonce", "Lemonade")
print(album1)
for album_n1 in album1.values():#在返回的字典中使用for循环，遍历字典的值，即只输出album1的值
    print(album_n1)

print('\n')
#专辑2
def make_album(singer_name,singer_album,number_song=''):
    albums={'name':singer_name,'album':singer_album}
    if number_song:
        albums['number_song'] = number_song
    return albums
while True:
    name = input('please input a name:')
    if name == 'q':
        break
    album_name = input('please input a album_name:')
    if album_name == 'q':
        break
    album_input = make_album(name,album_name)#这里是input的实参，但是开头定义的函数ablums的形参才是字典的键）
    print(album_input)
    print('my favorite singer is '+album_input['name'])
    print('I love her/his '+album_input['album'] )
    