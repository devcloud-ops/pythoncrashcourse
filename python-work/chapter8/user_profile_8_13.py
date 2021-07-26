# 8-13. User Profile: Start with a copy of user_profile.py from page 149. 
# Build a profile of yourself by calling build_profile(), using your first and 
# last names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info): #The
# double asterisks before the parameter **user_info cause Python to create
# an empty dictionary called user_info and pack whatever name-value pairs
# it receives into this dictionary
        
    """Builds a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    for k,v in user_info.items():
        if k != 'learning':
            print("{} is {}".format(k,v))
        else:
            print("{} {}".format(k,v))
    return user_info

user_profile = build_profile('muhammad faisal', 'siddiqui',location='melbourne',
                             field='devops', learning='python')
print(user_profile)