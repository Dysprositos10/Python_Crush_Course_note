def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

def make_car(Manufacturer_info,model_info,**user_info):
    car={}
    car['Manufacturer'] = Manufacturer_info
    car['model'] = model_info
    for key,value in user_info.items():#方法items(),它返回一个键—值对列表
        car[key] = value
    return car