import pizza #模块是扩展名为.py的文件,import语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from module_name import function_name 导入模块中的特定函数
#from module_name import function_0,function_1,function_2 从模块中导入任意数量的函数
from pizza import make_pizza #模块中多个函数，只导入想要使用的函数
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_car#注意，导入时要保证模块是已保存
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

from pizza import make_pizza as mp #as将函数重命名为你提供的别名
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

import pizza as p #as也可将模块重命名为你提供的别名
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import * #星号（*）运算符可让python导入模块中的所有函数
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')