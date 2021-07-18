# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of 
# users is not empty.
# a) If the list is empty, print the message We need to find some users!
# b) Remove all of the usernames from your list, and make sure the correct
# message is printed.

# usernames = ['mansoor', 'faisal', 'salman', 'fahad', 'admin']
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            greetings_message1 = ' '.join((f"Hello {username}, would you like to",
                                        "see a status report?"))
            print(greetings_message1)
        else:
            greetings_message2 = ' '.join((f"Greetings {username}, thank you",
                                        "for logging in again!"))
            print(greetings_message2)
else:
    print('\nWe need to find some users!')