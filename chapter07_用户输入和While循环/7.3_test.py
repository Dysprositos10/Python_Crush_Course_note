#熟食店
sandwich_orders=['egg','fish','pastrami']
finished_sandwiches=[]
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print('I made your '+finished_sandwich+' sandwich') 
    finished_sandwiches.append(finished_sandwich)
print("\nThere are many sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
print('I finished your '+','.join(finished_sandwiches)+' sandwiches') #join()函数连接列表里面所有元素


print('\n')
print('\n')
print('\n')

#五香烟熏牛肉（pastrami）卖完了
sandwich_orders=['egg','fish','pastrami']
finished_sandwiches=[]
print('The pastrami is sell out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich) #for循环也可以添加列表元素，只是不修改原有的列表
print('we only have '+','.join(finished_sandwiches)+' sandwiches') 


print('\n')
print('\n')
print('\n')
#度假调查
vacationlands={}
polling_active = True
while polling_active:
    name=input('what is your name: ')
    vacation=input('If you could visit one place in the world, where would you go?')
    vacationlands[name]=vacation
    repeat=input('Would you like to let another person respond? (yes/ no)  ')
    if repeat == 'no':
        polling_active = False
print('\n poll results:')
for name, vacation in vacationlands.items():#没有for循环遍历结果的话，只输出最后一个while循环的键值对
    print(name+' want to go '+vacation)