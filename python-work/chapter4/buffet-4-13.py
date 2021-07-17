# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.

# • Use a for loop to print each food the restaurant offers.

# • Try to modify one of the items, and make sure that Python rejects the change.

# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

# Defining five_foods as tuple instead of a list, so food becomes immutable
five_foods = ('shawarma', 'kabsa', 'mandi', 'madghoot', 'madhbi')
for food in five_foods:
    print(f'\nWe offer {food.title()}')

# Not possible to modify tuple value. Traceback exception thrown.
# five_foods[1] = 'broasted'
# five_foods[2] = 'grilled_chicken'

five_foods = ('shawarma', 'broasted', 'grilled_chicken', 'madghoot', 'madhbi')
print('\nMenu has been updated...\n')
for food in five_foods:
    print(f'\nWe offer {food.title()}')