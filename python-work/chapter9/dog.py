class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self,name,age): # This method will run automatically upon 
        # instantiation because of its name "init" and the two leading and 
        # trailing underscores.
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulating a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulating rolling over in response to a command."""
        print(f"{self.name} just rolled over!")