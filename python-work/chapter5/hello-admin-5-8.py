# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting
# to each user:
# a) If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# b) Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.

usernames = ['mansoor', 'faisal', 'salman', 'fahad', 'admin']

for username in usernames:
    if username == 'admin':
        greetings_message1 = ' '.join((f"Hello {username}, would you like to",
                                       "see a status report?"))
        print(greetings_message1)
    else:
        greetings_message2 = ' '.join((f"Greetings {username}, thank you",
                                      "for logging in again!"))
        print(greetings_message2)

