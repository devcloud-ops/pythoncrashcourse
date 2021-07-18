## Storing one kind of information about many objects

# poll from a number of people about their favorite programming language
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print(favorite_languages)

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")