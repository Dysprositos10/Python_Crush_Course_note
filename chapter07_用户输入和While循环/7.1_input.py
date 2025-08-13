#函数input()的工作原理
prompt = "If you tell us who you are, we can personalize the messages you see." #input()接受一个参数：即要向用户显示的提示或说明，让用户知道该如何做
prompt += "\nWhat is your first name? "#运算符+=在存储在prompt中的字符串末尾附加一个字符串。
name = input(prompt)
print("\nHello, " + name + "!")

print('\n')
#使用 int()来获取数值输入
height = input("How tall are you, in inches? ")
height = int(height)#函数int()，它让Python将输入视为数值。(原来的字符串str变为数值int)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")#数值输入用于计算和比较前，务必将其转换为数值表示

print('\n')
#求模运算符
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:#求模运算符（%）将两个数相除并返回余数
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")