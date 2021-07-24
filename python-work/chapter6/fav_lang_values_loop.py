# poll from a number of people about their favorite programming language
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
    'alan': 'python'
    }

# for value in sorted(favorite_languages.values()):
#     print(f"{value.title()}")

# Output: 
# C
# Java  
# Python
# Python
# Ruby

# Get unique values:
for value in set(favorite_languages.values()):
    print(f"{value.title()}")

# Output: 
# C
# Ruby
# Java
# Python