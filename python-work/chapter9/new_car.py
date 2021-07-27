import car as c

my_new_car = c.Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())
# Output: 2019 Audi A4

# Modifying Attribute Value:

# Approach 1: Modifying an Attribute’s Value Directly:
# my_new_car.odometer_reading = 23

# Approach 2: Modifying an Attribute’s Value Directly:
# my_new_car.update_odometer(22)
# my_new_car.update_odometer(21) # can't rollback odometer

# Approach 3: Incrementing an Attribute’s Value Through a Method
my_new_car.update_odometer(20)
my_new_car.increment_odometer(30)

my_new_car.read_odometer()
# Output: This car has traveled 0 miles.

my_new_car.fill_gas_tank(30)
print(f"Gas tank has been filed with {my_new_car.liters} liters.")
