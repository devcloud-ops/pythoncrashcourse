# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# a) Make a list of five or more usernames called current_users.
# b) Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# c) Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# d) Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
# current_users containing the lowercase versions of all existing users.)

current_users = ['mAnsoor', 'faisaL', 'Salman', 'fahaD', 'Nauman']

# Creating a new list that stores case insensitive "current_users" list.
current_users_case_insensitive = []
for user in current_users:
    current_users_case_insensitive.append(user.lower())

# verify that the new list is indeed case insensitive
print(current_users_case_insensitive)

new_users = ['samir', 'umer', 'faisal', 'yasir', 'badar']
# new_users = []

# ensure that the current_users or new_users list aren't empty:
if new_users:
    for new_user in new_users:
        if new_user.lower() in current_users_case_insensitive:
            username_unavailable = ' '.join((f"Your entered username:{new_user}",
                                        "is already in use. Please provide",
                                        "a new username!"))
            print(username_unavailable)
        else:
            username_available = ' '.join(("Congratulations! this username:",
                                        f"{new_user} is available for use!"))
            print(username_available)
else:
    print('\nWe need to find some users!')