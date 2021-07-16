bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print(bicycles[2], bicycles[3])

# applying string functions to list elements
print(bicycles[0].title())
print(bicycles[1].capitalize())
print(bicycles[2].count('e'))
print(bicycles[3].upper())

# below also returns last element in the list.
print(bicycles[-1].upper())

# below also returns second last element in the list.
print(bicycles[-2].upper())

# Using f-string manipulation while retrieving the list item and applying string operation 'title' to it
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)


