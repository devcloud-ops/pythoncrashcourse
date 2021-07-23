# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

person_imran = {
    'first_name': 'berry',
    'last_name': 'chen',
    'age': 42,
    'city': 'xengiang'
}

# Display the entire dictionary to console
# print(person_imran)

# Below are two ways to retrieve the value of the key: first_name
# method 1: first_name = person_imran['first_name'].title()
# method 2: first = person_imran.get('first_name')

first = person_imran.get('first_name')
last = person_imran.get('last_name')
age = person_imran.get('age')
city = person_imran.get('city')

print(f'\nPerson\'s First Name is: {first.title()}')

print(f'\nPerson\'s Last Name is: {last.title()}')

print(f'\nPerson\'s Age is: {age}')

print(f'\nPerson\'s City is: {city.title()}')