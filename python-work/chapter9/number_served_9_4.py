# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business.

import resturant as r

res1 = r.Resturant('Bundoo Khan','Pakistani')
print(f"\nThis resturant has served {res1.number_served} customers.")
# Output:
# This resturant has served 0 customers.


res1.number_served = 30
print(f"\nThis resturant has served {res1.number_served} customers.")
# Output:
# This resturant has served 30 customers.


res1.set_number_served(50)
print(f"\nThis resturant has served {res1.number_served} customers.")
# Output:
# This resturant has served 50 customers.


res1.increment_number_served(50)
print(f"\nThis resturant has served {res1.number_served} customers.")
# Output:
# This resturant has served 100 customers.