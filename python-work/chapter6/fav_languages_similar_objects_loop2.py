## Storing one kind of information about many objects

# poll from a number of people about their favorite programming language
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
    }

# Loop through the favorite_languages dictionary and print the names of 
# everyone who took the poll

# You can choose to use the keys() method explicitly if it makes your code
# easier to read, or you can omit it if you wish.

for name in favorite_languages.keys():
    print(f"{name.capitalize()} took part in this fav langugage poll!")

# Output:
# Jen took part in this fav langugage poll!
# Sarah took part in this fav langugage poll!
# Edward took part in this fav langugage poll!
# Phil took part in this fav langugage poll!

print('\n')

# Testing the default behavior without "keys()" function, which should print
# the same output as above
for name in favorite_languages:
    print(f"{name.capitalize()} took part in this fav langugage poll!")

# Output:
# Jen took part in this fav langugage poll!
# Sarah took part in this fav langugage poll!
# Edward took part in this fav langugage poll!
# Phil took part in this fav langugage poll!

