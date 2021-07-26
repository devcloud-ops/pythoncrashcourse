def build_profile(first, last, **user_info): #The
# double asterisks before the parameter **user_info cause Python to create
# an empty dictionary called user_info and pack whatever name-value pairs
# it receives into this dictionary
        
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    for k,v in user_info.items():
        print("{} is {}".format(k,v))
    return user_info

user_profile = build_profile('albert', 'einstein',location='princeton',
                             field='physics')
print(user_profile)