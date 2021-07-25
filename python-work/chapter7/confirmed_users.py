# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users: # Run this loop until unconfirmed_users list is empty
    
    current_user = unconfirmed_users.pop()
    # pop() is an inbuilt function in Python that removes and returns last 
    # value from the list or the given index value. Parameter: index (optional)
    # The value at index is popped out and removed. If the index is not given,
    # then the last element is popped out and removed.
    
    print(f"\nVerifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
    # Display all confirmed users.
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())