# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ['chicken', 'beef', 'egg', 'vegetable', 'cheese',
                   'pastrami', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print(f"\nInitial order: {sandwich_orders}")

# No pastrami left
print("\nThe deli has run out of pastrami...")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(f"Removed pastrami sandwiches. \nNew list: {sandwich_orders}")
print("\n\n... ")

# Process rest of the sandwiches
print("Processing ordered sandwiches... ")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich.title()} Sandwich")
    finished_sandwiches.append(sandwich)
print("\n\n... ")
print("Following sandwiches were made: ")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")
