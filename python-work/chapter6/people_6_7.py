# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As 
# you loop through the list, print everything you know about each person.

berryc = {
    'first_name': 'berry',
    'last_name': 'chen',
    'age': 43,
    'city': 'melbourne'
}

# Make two new dictionaries representing different people
sofiet = {
    'first_name': 'sofie',
    'last_name': 'tran',
    'age': 42,
    'city': 'new york'
}

johnc = {
    'first_name': 'john',
    'last_name': 'carter',
    'age': 45,
    'city': 'london'
}

# store all three dictionaries in a list called people
people = [berryc, sofiet, johnc]

# Loop through your list of people. As  you loop through the list, print 
# everything you know about each person

for person in people:
    print(f"\nDetails of this person are:")
    for pii,data in person.items():
        if type(data) == str:
            print(f"\t{pii.title()} is {data.title()}")
        else:
            print(f"\t{pii.title()} is {data}")
