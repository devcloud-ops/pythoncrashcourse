# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message 
# indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class Resturant:
    """Creates a new resturant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize resturant name and its cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturant(self):
        """Displays resturant's name and cuisine type"""
        print(f"This resturant's name is: {self.restaurant_name.title()}.")
        print(f"{self.restaurant_name.title()} is a "
              f"{self.cuisine_type.title()} resturant.")
        
    def set_number_served(self,new_number):
        """Set the number of customers served by this resturant."""
        self.number_served = new_number
    
    def increment_number_served(self,updated_number):
        """Increments the number of customers served by this resturant."""
        self.number_served += updated_number
    
    def open_restaurant(self):
        """Informs users that the resturant is open"""
        print(f"{self.restaurant_name.title()} is open right now!")

class IceCreamStand(Resturant):
    """Ice cream stand as a specific kind of restaurant"""
    
    def __init__(self,restaurant_name, cuisine_type, *flavors):
        """Initializes attributes of this IceCreamStand"""
        super().__init__(restaurant_name, cuisine_type)
        # Initializes an additional list called flavors
        self.flavors = flavors
    
    def describe_resturant(self):
        """Displays resturant's name, cuisine type, and flavors"""
        super().describe_resturant()
        print(f"This Ice Cream Stand offers these flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor}")
            
    