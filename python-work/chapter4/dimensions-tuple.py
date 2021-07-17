# Tuples: sometimes you’ll want to create a list of items that cannot change. 
# Tuples allow you to do just that. Python refers to values that cannot
# change as immutable, and an immutable list is called a tuple.

# Defining Tuples: NOTICE: we use parentheses to define tuples instead of 
# square brackets (that's done in lists)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# If we attempt to change the value in a Tuple (which is by default immutable: can't be changed), 
# we get this Traceback exception:

# dimensions[1] = 250

# Traceback (most recent call last):
#   File "/python-work/chapter4/dimensions-tuple.py", line 15, in <module>
#     dimensions[1] = 250
# TypeError: 'tuple' object does not support item assignment

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

