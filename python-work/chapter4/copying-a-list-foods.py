# Copying a list:
my_foods = ['shawarma', 'falafel', 'shawwayah', 'kabsa', 'mandi', 'madghoot', 'madhbi']
print('\nMy favorite foods are: ')
print(my_foods)

# Below assignment will create friend_foods exactly same as my_foods
# friend_foods = my_foods

# Below assignment will create a unique friend_foods. That means, friend_foods will 
# from now onwards will maintain its own list.
friend_foods = my_foods[:]
print('\nMy friend\s favorite foods are: ')
print(friend_foods)

my_foods.append('broasted')
friend_foods.append('shees taook')

print('\nMy favorite foods are: ')
print(my_foods)

print('\nMy friend\s favorite foods are: ')
print(friend_foods)
