# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.

# • Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.

# • Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.

numbers = list(range(1,11))

cubes_first_3 = []
for value in numbers[:3]:
    cube = value**3
    cubes_first_3.append(cube)
print(f'\nThe first three cubes in the list are {cubes_first_3}')

cubes_middle_3 = []
for value in numbers[3:6]:
    cube = value**3
    cubes_middle_3.append(cube)
print(f'\nThe middle three cubes in the list are {cubes_middle_3}')

cubes_last_3 = []
for value in numbers[-3:]:
    cube = value**3
    cubes_last_3.append(cube)
print(f'\nThe last three cubes in the list are {cubes_last_3}')