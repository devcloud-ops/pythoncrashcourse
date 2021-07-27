# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically 
# stored in a user profile. Make a method called describe_user() that prints a 
# summary of the user’s information. Make another method called greet_user() 
# that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class User:
    """Creates user directory information"""
    
    def __init__(self, first_name, last_name, **user_profile):
        """Initializes various attributes of this class."""
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile = user_profile
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user profile attributes."""
        print(f"\nThis user's full name is: {self.first_name.title()} "
              f"{self.last_name.title()}. Other user profile data includes: ")
        for k,v in self.user_profile.items():
            print("\t{} is {}".format(k.title(),v.title()))

    def increment_login_attempts(self):
        """Increments the value of login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login attempts to 0"""
        self.login_attempts = 0

    def greet_user(self):
        """Greets a new user."""
        print(f"\nWelcome {self.first_name.title()} {self.last_name.title()}"
              " to this company!")