# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
# • Tests using the 'and' keyword and the 'or' keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list



# # • Tests for equality and inequality with strings
name = 'jace'
print(f'\nString Equality Test: Is the string same as \'jace\'?')
print(name == 'jace')
print(f'\nString Inequality Test: Is the string same as \'kelly\'?')
print(name != 'jace')

# • Tests using the lower() method
name = 'FaiSal'
print(f'\nString Equality Test using lower() function: Is the string same as \'faisal\'?')
print(name.lower() == 'faisal')

# • Tests using the 'and' keyword and the 'or' keyword
print('\nAge test using and / or keywords')
age = 40
print(age == 40 and age < 41) #Result should be True
print(age == 30 or age > 39) #Result should be True

# • Test whether an item is in a list
print('\nTest whether a food item is in the menu list!')
menu = ['shawarma', 'kabsa', 'mandi', 'madghoot', 'madhbi']
print(f'current menu: {menu}')
print('kabsa' in menu) # Prints True
print('broasted' in menu) # Prints False
print('broasted' not in menu) # Prints True
menu.append('broasted')
print(f'new menu: {menu}')
print('broasted' in menu) # Prints True
print('broasted' not in menu) # Prints False
