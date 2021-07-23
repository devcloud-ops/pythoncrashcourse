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

# Erin, you haven't participated in the poll, please do so!

for name in favorite_languages.keys():
    print(f'Hi {name.title()}.')
    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t {name.title()}, I see you love {language}!')

#output:
# Hi Jen.
#          Jen, I see you love Python! 
# Hi Sarah.
# Hi Edward.
# Hi Phil.
#          Phil, I see you love Java! 

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for takin the poll!")
    
# output: 
# Edward, thank you for takin the poll!
# Jen, thank you for takin the poll!   
# Phil, thank you for takin the poll!  
# Sarah, thank you for takin the poll! 