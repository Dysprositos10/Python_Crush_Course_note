from Restaurant import Restaurants as R 
Restaurant = R('老湘亲','湘菜')
Restaurant.describe_restaurant()
#类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。
#实例名和模块名都采用小写格式，并在单词之间加上下划线


print('\n')
#有序字典
from collections import OrderedDict #模块collections中的一个类——OrderedDict:能记录键—值对的添加顺序
favorite_languages = OrderedDict()#导入了OrderedDict类：不使用花括号，而是调用OrderedDict()来创建一个空的有序字典
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print('\n')
#骰子    
from random import randint
class Die():
    def __init__(self, sides = 6):
        """初始化描述汽车的属性"""
        self.sides = sides

    def roll_die(self):
        current_number = 1
        while True:
            x = randint(1, self.sides)
            print(x)
            current_number += 1
            if current_number == 11:
                break
die6 = Die(6)
die6.roll_die()
print('\n')

die6 = Die(20)
die6.roll_die()

#骰子2 
from random import randint
class Die():
    def __init__(self, sides=6):
        self.sides = sides
#在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类。
    def roll_die(self, times):
        for i in range(times):#函数range()让Python从指定的第一个值开始数，并在到达指定的第二个值后停止
            number = randint(1, self.sides)
            print("number is: " + str(number))
die1 = Die(6)
die1.roll_die(10)
print("\n")

die3 = Die(20)
die3.roll_die(10)
