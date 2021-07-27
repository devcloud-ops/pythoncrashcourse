class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Definition here will suffice with a default
                                  # value
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given miles to the odometer reading."""
        self.odometer_reading += miles

    def read_odometer(self):
        """Displays car's mileage."""
        print(f"This car has traveled {self.odometer_reading} miles.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric cars."""
    
    def __init__(self,make,model,year):
        """Initialize attributes of the parent class"""
        super().__init__(make,model,year)