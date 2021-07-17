motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#to modify an element in a list, specify the list element with index and assign it a new value
motorcycles[0] = 'ducati'
print(motorcycles)

#adding elements to a list
motorcycles.append('honda')
print(motorcycles)

#removing first occurence of an elements from a list
motorcycles.remove('honda')
print(motorcycles)

#adding elements to a list
motorcycles.append('honda')
motorcycles.append('honda')
print(motorcycles)

#counting elements in a list
print(motorcycles.count('honda'))

#find the length (number of elements) in a list
print(len(motorcycles))

# insert an element to any position inside the element
motorcycles.insert(3,'suzuki')
print(motorcycles)

motorcycles.insert(3,'suzuki')
print(motorcycles)

#counting elements in a list
print(motorcycles.count('suzuki'))

#find the length (number of elements) in a list
print(len(motorcycles))

#delete a specific element (with certain index) from the list:
del motorcycles[2]
print(motorcycles)
