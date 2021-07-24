# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers_country = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
for k,v in rivers_country.items():
    print(f'The {k.capitalize()} runs through {v.capitalize()}!')
# Output
# The Nile runs through Egypt!
# The Amazon runs through Brazil!
# The Yangtze runs through China!

print('\n')

# • Use a loop to print the name of each river included in the dictionary.
for river in rivers_country.keys():
    print(f'{river.capitalize()}')
# Output
# Nile
# Amazon
# Yangtze

print('\n')

# • Use a loop to print the name of each country included in the dictionary.
for country in rivers_country.values():
    print(f'{country.capitalize()}')

# Output
# Egypt
# Brazil
# China