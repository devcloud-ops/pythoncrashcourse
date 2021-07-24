# Store information about a pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'chillis'],
}

# Summarize the order
print(f"\nYou ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

# Available toppings
for topping in pizza['toppings']:
    #print(f'Topping: {topping.title()}')
    print(f'\t' + topping)

# Output: 
#
# You ordered a thick-crust pizza with the following toppings:
#         mushrooms
#         extra cheese
#         chillis