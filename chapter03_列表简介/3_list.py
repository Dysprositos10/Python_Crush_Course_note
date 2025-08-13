#访问列表元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] #方括号（[]）来表示列表，并用逗号来分隔其中的元素
print(bicycles[0])
print(bicycles[1].title())#方括号中指出元素索引,第一个元素索引为0
print(bicycles[-1])#-1为最后一个元素

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

#修改、添加和删除列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')#方法append()添加至列表末尾
print(motorcycles)
motorcycles.insert(0, 'ducati')#方法insert()插入
print(motorcycles)
del motorcycles[0]# del语句用于删除，不可再使用
print(motorcycles)
last_owned= popped_motorcycle = motorcycles.pop()#方法pop()可删除列表末尾的元素，并且可以存储到变量中
print(motorcycles)
print(popped_motorcycle)
print("The last motorcycle I owned was a " + last_owned.title() + ".")
first_owned = motorcycles.pop(0)#可指定要删除的元素的索引
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#方法remove()不知道元素位置，可根据值删除元素，若有重复，只删除第一个指定的值
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove('ducati')
print(motorcycles)
print("A " + too_expensive.title() + " is too expensive for me.")
print("\nA " + too_expensive.title() + " is too expensive for me.")#开头加上\n换行符会多一个空行

print("\n")
print("\n")
print("\n")
#测试
lanch=["a","b","c"]#不加括号会变成一整个输出是a b c 字符串，而不是a字符串………要注意中间间隔是逗号
print(lanch)
lanch[0]='D'
print(lanch)
lanch.insert(0,'1')
print(lanch)
print("我只能邀请两位")
pop=lanch.pop()
print(pop)
print(pop+"我很抱歉你不能来")
print(lanch[1]+"你依然可以来")
del lanch[0]
print(lanch)
del lanch[0]
del lanch[0]
print(lanch)

print("\n")
print("\n")
print("\n")
#组织列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)#sort()按照字母顺序永久性排序
cars.sort(reverse=True)#sort()按照字母倒序永久性排序
print(cars)
print("\n")
print("\n")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))#函数sorted()对列表进行临时排序
print("\nHere is the original list again:")
print(cars)
cars.reverse()#方法reverse()按相反的顺序永久性排列
print(cars)
len(cars)#交互式环境（如Jupyter Notebook、Python Shell）直接输入 len(hobb) 会返回结果 
print(len(cars))#脚本文件运行（如.py文件）：必须使用 print() 才能显示结果，否则计算后结果会被丢弃。
print("\n")
print("\n")
print("\n")
#测试
place=['xiamen','nanjing','shanghai','guangzhou','chongqing']
print(place)
print(sorted(place))
print(place)

place.reverse()
print(place)
place.reverse()
print(place)
place.sort
print(len(place))