#requested_topping = 'mushrooms'

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
requested_toppings = []

# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# if 'mushrooms' in requested_topping:
#     print('great job, proceed with the order!')

# When the name of a list is used in an if statement, Python returns True if 
# the list contains at least one item; an empty list evaluates to False.
    
if requested_toppings:  # This condition checks if requested_toppings isn't 
                        # empty
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("\nSorry, we are out of green peppers right now.")
        else:
            print(f"\nAdding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
