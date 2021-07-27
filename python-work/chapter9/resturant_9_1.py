# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message 
# indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

import resturant as r

print("\n\n")

resturant1 = r.Resturant('gulf royal chinese resturant','chinese')
print(f"{resturant1.restaurant_name.title()}")
print(f"{resturant1.cuisine_type.title()}")
resturant1.describe_resturant()
resturant1.open_restaurant()

print("\n\n")

resturant2 = r.Resturant('bundoo khan','pakistani')
print(f"{resturant2.restaurant_name.title()}")
print(f"{resturant2.cuisine_type.title()}")
resturant2.describe_resturant()
resturant2.open_restaurant()