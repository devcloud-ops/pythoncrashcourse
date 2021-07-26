# 8-14. Cars: Write a function that stores information about a car in a 
# dictionary. The function should always receive a manufacturer and a model 
# name. It should then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value 
# pairs, such as a color or an optional feature. Your function should work for
# a call like this one: 
# ____________________________________________________________________
# car = make_car('subaru', 'outback', color='blue', tow_package=True) 
# ____________________________________________________________________
# Print the dictionary that’s returned to make sure all 
# the information was stored correctly.



def make_car(manufacturer, model, **car_info):
    """Stores and returns a dictionary detail of cars"""
    car_info['Manufacturer'] = manufacturer
    car_info['Model'] = model
    return car_info

def display_car(car):
    """Prints car details"""
    print("\nThis car's specifications are as follows:")
    for k,v in car.items():
        if v == True:
            print(f"\t{k} is included")
        else:
            print("\t{} is {}".format(k.title(), v.title()))


car1 = make_car('subaru', 'outback', color='blue', tow_package=True) 
display_car(car1)

car2 = make_car('toyota', 'camry', color='black', tow_package=True) 
display_car(car2)

car3 = make_car('mercedez', 'benz s-class', color='silver') 
display_car(car3)

# Output:

# This car's specifications are as follows:
#         Color is Blue
#         tow_package is included
#         Manufacturer is Subaru
#         Model is Outback

# This car's specifications are as follows:
#         Color is Black
#         tow_package is included
#         Manufacturer is Toyota
#         Model is Camry

# This car's specifications are as follows:
#         Color is Silver
#         Manufacturer is Mercedez
#         Model is Benz S-Class
