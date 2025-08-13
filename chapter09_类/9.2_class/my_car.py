from car import Car #import语句让Python打开模块car，并导入其中的Car类,注意import要先保存
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 2
my_new_car.read_odometer()

print('\n')
from car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print('\n')
from car import Car, ElectricCar #从一个模块中导入多个类时，用逗号分隔各个类
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

print('\n')
import car #导入整个模块
my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

print('\n')
from car import Car
from electriccar import ElectricCar as EC # type: ignore,给 ElectricCar 这个类指定一个别名：
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = EC('tesla', 'roadster', 2018)
print(my_tesla.get_descriptive_name())

print('\n')
from car import Car
import electriccar as ec # type: ignore，导入模块 electriccar 并给它指定了别名：
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ec.ElectricCar('tesla', 'roadster', 2018)#模块别名和模组全名
print(my_tesla.get_descriptive_name())