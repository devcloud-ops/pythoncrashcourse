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
