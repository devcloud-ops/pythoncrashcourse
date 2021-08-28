# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class 
# you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either 
# version of the class will work; just pick the one you like better. Add an 
# attribute called flavors that stores a list of ice cream flavors. Write a 
# method that displays these flavors. Create an instance of IceCreamStand, 
# and call this method.

import resturant as r


#Parent class instantiation works
resturant1 = r.Resturant('ABC Resturant','Asian Cuisine')
resturant1.describe_resturant()

# Output: 
# This resturant's name is: Abc Resturant.
# Abc Resturant is a Asian Cuisine resturant.


#Child class instantiation breaks
icecreamstand1 = r.IceCreamStand('Baskin Robins','Ice Cream Stand', 'vanilla', 
                                 'strawberry', 'chocolate', 'mango')

icecreamstand1.describe_resturant()
# Output:
# This resturant's name is: Baskin Robins.
# Baskin Robins is a Ice Cream Stand resturant.
# This Ice Cream Stand offers these flavors: 
# line 49, in describe_resturant
#     for flavor in flavors:
# NameError: name 'flavors' is not defined
