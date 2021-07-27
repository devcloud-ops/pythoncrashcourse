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