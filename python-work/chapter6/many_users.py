# Dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

# for username, users_info in users.items():
#     print(f'\nUsername: {username.title()}')
#     for property,value in users_info.items():
#         print(f'{property.title()}: {value.title()}')

for username, users_info in users.items():
    print(f'\nUsername: {username}')
    print(f"Full Name: {users_info['first'].title()} {users_info['last'].title()}")
    print(f"User's Current Location: {users_info['location'].title()}")
