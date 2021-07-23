## Storing one kind of information about many objects

# poll from a number of people about their favorite programming language
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
    }

print(favorite_languages)

#######################################################################
# Manually fetching and printing the dictionary key:value pairs

# jen_fav = favorite_languages['jen'].title()
# sarah_fav = favorite_languages['sarah'].title()
# edward_fav = favorite_languages['edward'].title()
# phil_fav = favorite_languages['phil'].title()

# print(f"Jen's favorite language is {jen_fav}.")
# print(f"Sarah's favorite language is {sarah_fav}.")
# print(f"Edwards's favorite language is {edward_fav}.")
# print(f"Phil's favorite language is {phil_fav}.")

#######################################################################
# Using a loop to print the same reduces the code from 8 lines to lines!
# If a dictionary had million of items, below is the only feasible way!

for name,language in favorite_languages.items():
    print(f"{name.capitalize()}'s favorite language is {language.capitalize()}")


