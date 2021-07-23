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
for name in favorite_languages.keys():
    print(f"{name.capitalize()} took part in this fav langugage poll!")


