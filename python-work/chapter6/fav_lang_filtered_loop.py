# poll from a number of people about their favorite programming language
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
    }

friends = ['jen','phil']

if 'erin' not in favorite_languages.keys():
        print("Erin, you haven't participated in the poll, please do so!\n")

for name in favorite_languages.keys():
    print(f'Hi {name.title()}.')
    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t {name.title()}, I see you love {language}!')
