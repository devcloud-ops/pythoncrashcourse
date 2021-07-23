# poll from a number of people about their favorite programming language
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
    }

for value in sorted(favorite_languages.values()):
    print(f"{value.title()}")

# Output: 
# C
# Java  
# Python
# Ruby