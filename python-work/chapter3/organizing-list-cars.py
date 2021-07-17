###################### Organizing Lists #######################

#Using sort() method on lists to sort them permanently in alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'\nBefore sorting the cars in alphabetical order: {cars}')

cars.sort()
print(f'After sorting the cars in alphabetical order: {cars}\n')

alphabets=['c','e','d','a','z','b','y']
print(f'Before sorting the alphabets in alphabetical order: {alphabets}')

alphabets.sort()
print(f'After sorting the alphabets in alphabetical order: {alphabets}\n')


#Using sort() method on lists to sort them permanently in 'reverse' alphabetical order

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'Before sorting the cars in reverse alphabetical order: {cars}')

cars.sort(reverse=True)
print(f'After sorting the cars in reverse alphabetical order: {cars}\n')

alphabets=['c','e','d','a','z','b','y']
print(f'Before sorting the alphabets in reverse alphabetical order: {alphabets}')

alphabets.sort(reverse=True)
print(f'After sorting the alphabets in reverse alphabetical order: {alphabets}\n')

############################################################################################

print ('\n\n--------------------------------------------------------------------------\n\n')

############################################################################################

#Using sorted() method on lists to sort them temporarily in alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'\nBefore sorting the cars in temporarily in alphabetical order: {cars}')

sorted(cars) #The changes to the cars list is valid and applicable till this line only
print(f'During sorting the cars temporarily in alphabetical order: {sorted(cars)}')
print(f'After sorting the cars in alphabetical order: {cars}\n')


alphabets=['c','e','d','a','z','b','y']
print(f'Before sorting the alphabets in alphabetical order: {alphabets}')

sorted(alphabets)#The changes to the alphabets list is valid and applicable till this line only
print(f'During sorting the alphabets temporarily in alphabetical order: {sorted(alphabets)}')
print(f'After sorting the alphabets in alphabetical order: {alphabets}\n')

############################################################################################

print ('\n\n--------------------------------------------------------------------------\n\n')

############################################################################################

#Using sorted() method on lists to sort them temporarily in reverse alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'\nBefore sorting the cars temporarily in reverse alphabetical order: {cars}')

sorted(cars, reverse=True) #The changes to the cars list is valid and applicable till this line only
print(f'During sorting the cars temporarily in reverse alphabetical order: {sorted(cars, reverse=True)}')
print(f'After sorting the cars in reverse alphabetical order: {cars}\n')


alphabets=['c','e','d','a','z','b','y']
print(f'Before sorting the alphabets in reverse alphabetical order: {alphabets}')

sorted(alphabets, reverse=True)#The changes to the alphabets list is valid and applicable till this line only
print(f'During sorting the alphabets temporarily in reverse alphabetical order: {sorted(alphabets, reverse=True)}')
print(f'After sorting the alphabets in reverse alphabetical order: {alphabets}\n')


