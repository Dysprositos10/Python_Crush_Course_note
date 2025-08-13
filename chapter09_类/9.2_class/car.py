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
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
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