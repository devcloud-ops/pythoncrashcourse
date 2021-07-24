# 6-8. Pets: Make several dictionaries, where each dictionary represents a 
# different pet. In each dictionary, include the kind of animal and the 
# owner’s name. Store these dictionaries in a list called pets. Next, loop 
# through your list and as you do, print everything you know about each pet.

pet1 = {
    'owner name': 'mansoor siddiqui',
    'kind': 'cat'
}

pet2 = {
    'owner name': 'faisal siddiqui',
    'kind': 'dog'
}

pet3 = {
    'owner name': 'salman siddiqui',
    'kind': 'bird'
}

pet4 = {
    'owner name': 'fahad siddiqui',
    'kind': 'fish'
}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print(f"{pet['owner name'].title()} owns a {pet['kind'].capitalize()}! ")