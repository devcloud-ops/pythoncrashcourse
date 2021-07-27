# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically 
# stored in a user profile. Make a method called describe_user() that prints a 
# summary of the user’s information. Make another method called greet_user() 
# that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

import users as u

user1 = u.User('mansoor','siddiqui', title='senior manager',
               department='SAP MM', division='it shared services')

user1.describe_user()
user1.greet_user()

user2 = u.User('faisal','siddiqui', title='lead consultant',
               department='platform engineering', division='it shared services')

user2.describe_user()
user2.greet_user()

user3 = u.User('salman','siddiqui', title='regional head',
               department='chemical sales', division='business development')

user3.describe_user()
user3.greet_user()