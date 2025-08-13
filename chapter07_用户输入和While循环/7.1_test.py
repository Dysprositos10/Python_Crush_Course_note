#餐馆订位
people=input('May I ask how many people are dining: ')
people=int(people)
if people > 8:
    print('There are no available tables')
else:
    print('There is a table available')

    
print('\n')
#10的整数倍
number=input('please inter a number: ')
number=int(number)
if number%10==0:
    print('true')
else:
    print('false')
