# 6-6. Polling: Use the code in favorite_languages.py (page 97).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
    'alan': 'python',
    'caroline': 'html',
    'ben': 'typescript',
    'alex': 'php',
    'scott': 'javascript',
    }


# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
people_for_polling = ['jen','sarah','edward','phil','alan','caroline','ben',
                      'alex','scott','faisal','mansoor','salman','fahad']

print(people_for_polling)

# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

for person in people_for_polling:
    if person in favorite_languages.keys():
        print(f'Dear {person.capitalize()}, thank you for taking the poll!')
    else:
        print(f'Dear {person.capitalize()}, you are invited to take the poll!')