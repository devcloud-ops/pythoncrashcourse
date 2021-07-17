# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.

# • Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.

# • Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.

numbers = list(range(1,11))

cubes = []
for value in numbers:
    cube = value**3
    cubes.append(cube)

print(f'\nList of all cubes from 1 to 10 is: {cubes}\n')
print(f'\nFirst three cubes from 1 to 10 are: {cubes[:3]}\n')
print(f'\nMiddle three cubes from 1 to 10 are: {cubes[3:6]}\n')
print(f'\nLast three cubes from 1 to 10 are: {cubes[-3:]}\n')
