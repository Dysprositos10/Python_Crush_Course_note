class Dog():#首字母大写的名称指的是类。这个类定义中的括号是空的，要从空白创建这个类
    #类=有关如何创建实例的说明
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):#类中的函数称为方法，_init_第一个参数必须是 self，用于指向即将创建的实例对象
        #开头和末尾各有两个下划线，方法可以接收多个参数，用于为对象赋初值
        """初始化属性name和age"""
        self.name = name
        self.age = age#以self为前缀的变量都可供类中的所有方法使用，这些能够通过实例访问的变量称为属性
        #通过实参向Dog()传递名字和年龄；self会自动传递，我们不需要传递它。
    def sit(self):    
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
my_dog = Dog('willie', 6)#小写的名称（如my_dog）指的是根据类创建的实例
#方法__init__()并未显式地包含return语句，但Python自动返回一个表示这条小狗的实例
#我们将这个实例存储在变量my_dog中。
print("My dog's name is " + my_dog.name.title() + ".")
#句点就是汉语语法中的“的”字，在Dog类中引用name属性时，使用的是self.name
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

print('\n')
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

print('\n')
#餐馆
class Restaurants():
    def __init__(R,restaurant_name,cuisine_type):
        R.restaurant_name=restaurant_name
        R.cuisine_type=cuisine_type
    def describe_restaurant(R):
        print('The name of the restaurant is '+R.restaurant_name.title())
        print('The type of the restaurant is '+R.cuisine_type.title())
    def open_restaurant(R):
        print('\nThe restaurant is open')
Restaurant = Restaurants('老湘亲','湘菜')
Restaurant.describe_restaurant()
Restaurant.open_restaurant()

print('\n')
#用户
class Users():
    def __init__(U,first_name,last_name):
        U.first_name = first_name
        U.last_name = last_name#Python解释器都会自动将实例对象作为第一个参数传给方法
    def describe_user(U):
        print('User:'+U.first_name+' '+U.last_name)
    def greet_user(U):
        print('Welcome!'+U.first_name+' '+U.last_name)
user = Users('john','balo')
user.describe_user()
user.greet_user()

print('\n')
#用户2 优化
class Users():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name#Python解释器都会自动将实例对象作为第一个参数传给方法
        # 将 full_name 保存为实例属性：也储存在self中
        self.full_name = self.first_name + " " + self.last_name  # 添加空格分隔
    def describe_user(self):
        print('User:'+self.full_name)
    def greet_user(self):
        print('Welcome!'+self.full_name)
user = Users('john','balo')
user.describe_user()
user.greet_user()


print('\n')#Car类等同于
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        self.long_name = str(self.year) + ' ' + self.make.title() + ' ' + self.model.title()
        print(self.long_name)
my_new_car = Car('audi', 'a4', 2016)
my_new_car.get_descriptive_name()

#Car类1
print('\n')
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23 #通过访问直接修改属性的值
my_new_car.read_odometer()

#Car类2：通过方法修改属性的值
print('\n')
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)#提供了实参23 （对应形参mileage）
my_new_car.read_odometer()
my_new_car.update_odometer(13)#新指定的里程（mileage）小于原来的里程（self.odometer_reading）

#Car类3：通过方法对属性的值进行递增
print('\n')
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        if miles >= 0:
            self.odometer_reading += miles #接受一个数字，通过+=将其加入到self.odometer_reading中 
        else:
            print("You can't roll back an odometer!")
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#就餐人数
print('\n')
class Restaurants():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print('The name of the restaurant is '+self.restaurant_name.title())
        print('The type of the restaurant is '+self.cuisine_type.title())
    def open_restaurant(self):
        print('The restaurant is open')
    def restaurant_people(self):
        print('There are '+str(self.number_served)+' people')
Restaurant = Restaurants('老湘亲','湘菜')
Restaurant.describe_restaurant()
Restaurant.open_restaurant()
Restaurant.number_served = 23
Restaurant.restaurant_people()

#就餐人数2
print('\n')
class Restaurants():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print('The name of the restaurant is '+self.restaurant_name.title())
        print('The type of the restaurant is '+self.cuisine_type.title())
    def open_restaurant(self):
        print('The restaurant is open')
    def set_number_served(self,people):
         self.number_served=people
         print('There are '+str(self.number_served)+' people')
    def increment_number_served(self,increment_people):
        self.number_served += increment_people
        print('There should be '+str(self.number_served)+' guest today')
Restaurant = Restaurants('老湘亲','湘菜')
Restaurant.describe_restaurant()
Restaurant.open_restaurant()
Restaurant.set_number_served(2)
Restaurant.increment_number_served(5)

#尝试登录次数
print('\n')
class Users():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name#Python解释器都会自动将实例对象作为第一个参数传给方法
        # 将 full_name 保存为实例属性：也储存在self中
        self.full_name = self.first_name + " " + self.last_name  # 添加空格分隔
        self.login_attempts = 0
    def describe_user(self):
        print('User:'+self.full_name)
    def greet_user(self):
        print('Welcome!'+self.full_name)
    def increment_login_attempts(self):
        self.login_attempts += 1
        print('Current login times:'+str(self.login_attempts))
    def reset_login_attempts(self):
        self.login_attempts = 0
        print('Login times reset to '+str(self.login_attempts))
user = Users('Landon','Leo')
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()


#Car类4：继承类
print('\n')
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        if miles >= 0:
            self.odometer_reading += miles #接受一个数字，通过+=将其加入到self.odometer_reading中 
        else:
            print("You can't roll back an odometer!")
    def fill_gas_tank(self):
        print("This car need a gas tank")
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):#这个形参是可选的：如果没有给它提供值，电瓶容量将被设置为70。
        """初始化电瓶的属性"""
        self.battery_size = battery_size 
    def describe_battery(self,R):
        """打印一条描述电瓶容量的消息"""
        self.battery_size = R#如果增加一个形参，引用时就必须加上指定值，不会默认
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        """检查电瓶容量,如果不是85就将设置为85"""
        if self.battery_size != 85:
            self.battery_size =85
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):#子类ElectricCar的__init__
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)#在子类中，通过super()调用父类Car的__init__
        self.battery = Battery()# Battery实例存储在属性self.battery中
        #每个ElectricCar实例都包含一个自动创建的Battery实例
    def fill_gas_tank(self):#重写父类的方法
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery(70)
#在实例my_tesla中查找属性battery，并对存储在该属性中的Battery实例调用方法describe_battery()。
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


#冰淇淋小店
print('\n')
class Restaurants():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print('The name of the restaurant is '+self.restaurant_name.title())
        print('The type of the restaurant is '+self.cuisine_type.title())
    def open_restaurant(self):
        print('The '+self.restaurant_name+' is open')
    def set_number_served(self,people):
         self.number_served=people
         print('There are '+str(self.number_served)+' people')
    def increment_number_served(self,increment_people):
        self.number_served += increment_people
        print('There should be '+str(self.number_served)+' guest today')
class IceCreamStand(Restaurants):
    def __init__(self, restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors =['banana','apple','mike']
    def describe_icecream(self):
        print(', '.join(self.flavors))#用join()方法一次性拼接成一个字符串，而不是在循环中逐行打印
    def describe_icecream2(self):
        for self.flavor in self.flavors:
            print('we have '+self.flavor+' icecream')
ice = IceCreamStand('DQ','冰淇淋店')
ice.describe_restaurant()
ice.open_restaurant()
ice.describe_icecream()
ice.describe_icecream2()

#管理员
print('\n')
class Users():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name#Python解释器都会自动将实例对象作为第一个参数传给方法
        # 将 full_name 保存为实例属性：也储存在self中
        self.full_name = self.first_name + " " + self.last_name  # 添加空格分隔
    def describe_user(self):
        print('User:'+self.full_name)
    def greet_user(self):
        print('Welcome!'+self.full_name)
class Privileges():
    def __init__(self,privileges = ['can add post','can delete post','can ban user'] ):
        #实例调用方法时，形参必须提前给定好参数在init中
        self.privileges = privileges 
    def show_privileges(self):
        for self.privilege in self.privileges:
            print('You have permission:'+self.privilege)
class Admin(Users):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)#init两边是两个下划线，且super继承的形参不需要self了
        self.Privileges = Privileges()
user = Admin('john','balo')
user.describe_user()
user.greet_user()
user.Privileges.show_privileges()