# Prints result of admission based on age

# age = 3
# age = 16
# age = 30
age = 67

# Approach 1
# if age < 4:
#     print('\nYour admission cost is $0.')
# elif age < 18:
#     print('\nYour admission cost is $25.')
# else:
#     print('\nYour admission cost is $40.')


# Approach 2: More appropriate
if age < 4:
    price = 0 # babies are exempted
elif age < 18:
    price = 25 # children and teen
elif age < 65:
    price = 40 # adult
else:
    price = 20 # seniors discount
    print('\nSeniors discount applied!')

print(f'\nYour admission cost is ${price}.')