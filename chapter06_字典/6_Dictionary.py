alien_0 = {'color': 'green', 'points': 5}#字典用花括号{}中的一系列键—值对
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
alien_0['x_position'] = 0#添加键值对
alien_0['y_position'] = 25
print(alien_0)
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'#修改键值对
print('\n'"The alien is now " + alien_0['color'] + ".")

print('\n')
print('\n')
print('\n')
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))# 向右移动外星人
alien_0['speed'] = 'fast'
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:#这个外星人的速度一定很快
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

print('\n')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points'] #del删除键值对（永远消失）
print(alien_0)

print('\n')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}#多行来定义字典时，在输入左花括号后按回车键，再在下一行缩进四个空格
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")#拼接运算符（+）后按回车键进入print语句的后续各行，

print('\n')
print('\n')
print('\n')
#测试
message={'first_name':'john','age':'18','city':'England'}
print(message['city'])
print('\n')
Vocabulary={'字符串':'str()','删除':'del()'}
print(Vocabulary['字符串'])



print('\n')
print('\n')
print('\n')
#遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():#方法items(),它返回一个键—值对列表
    print("\nKey: " + key)
    print("Value: " + value)
print('\n')
print('\n')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")
for name in favorite_languages.keys():#方法keys()遍历字典中的所有键(遍历字典时，会默认遍历所有的键,不加key也可以)
    print(name.title())
print('\n')
print('\n')


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")

print('\n')
print('\n')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):#函数sorted()让Python列出字典中的所有键，并在遍历前对这个列表进行排序（字母顺序）
    print(name.title() + ", thank you for taking the poll.") 
print("The following languages have been mentioned:")
for language in favorite_languages.values():#遍历字典中的值
    print(language.title())

print('\n')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):#set()，可让Python找出列表中独一无二的元素来创建一个集合
    print(language.title())


print('\n')
print('\n')
print('\n')
#测试，词汇表2
dic={'append':'添加',
     'range':'范围',
     'sort':'排序',
     'del':'删除',
     'pop':'末尾删除',}
for x,y in dic.items():
    print(x+':'+y)
print('\n')

river={'nile':'Egypt' , 'Mississippi' : 'America' , 'Amazon': 'Spain' }
for x,y in river.items():
    print('the '+x.title()+' runs through '+y)

print('\n')
print('\n')
print('\n')
#将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套   
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print('\n')
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(0,6):#循环5次创建
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)#在新创建的列表中加入for循环的结果
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))

print('\n')
print('\n')
print('\n')
#在字典中存储列表；需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表
# 存储所点比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

print('\n')
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
            print(name.title() + 's favorite language is '+languages[0].title()) 
    else:
            print("\n" + name.title() + "'s favorite languages are:")
            for language in languages:
                print("\t" + language.title())

print('\n')
print('\n')
print('\n')
#在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
}#储存的字典包含用户的名、姓和居住地
for username, user_info in users.items():#username储存键，'mcurie'储存值（字典）
    print("\nUsername: " + username)#输出键
    full_name = user_info['first'] + " " + user_info['last']#访问储存字典的值
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


print('\n')
print('\n')
print('\n')
#测试:people
new_message0={'first_name':'john','age':'18','city':'England'}
new_message1={'first_name':'anh','age':'20','city':'China'}
new_message2={'first_name':'lucy','age':'13','city':'USA'}
messages = [new_message0,new_message1,new_message2]
for message in messages:
    print(message)

print('\n')
#测试:pet
dog={'dog':'john'}
cat={'cat':'anh'}
bird={'bird':'lucy'}
pets=[dog,cat,bird]
for x in pets:
    print(x)

print('\n')
favourite_places = {
    'Bob' : ['Beijing','Shanghai','Guangzhou'],
    'Kevin' : ['Chongqing','Xian','Harbin'],
    'Stuart' : ['Chengdu' ,'Guilin' ,'Xiamen']
}
for x,place in favourite_places.items():
    print(x+' favorite place are: ')
    for y in place:
        print(y)

print('\n')   
cities = {
    'Beijing': { 'Country':'China','population':21730000,'fact':'the center of politics'},
    'Shanghai': { 'Country':'China','population':24200000,'fact':'the center of economy'},
    'Guangzhou' : {'Country':'China','population':14490000,'fact':'the center of exportation'},
}
for city,city_info in cities.items():
    print('\ncity:'+city)
    print('Country:'+city_info['Country']+
        ' \npopulation:'+str(city_info['population'])+
        ' \nfact:'+city_info['fact'])

print('\n')
#get()函数返回值：在指定的键不存在时返回一个默认值。
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
#第一个参数用于指定键，是必不可少的；第二个参数为当指定的键不存在时要返回的值
print(point_value)
