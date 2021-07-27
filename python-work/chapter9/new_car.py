import car as c

my_new_car = c.Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())
# Output: 2019 Audi A4

my_new_car.read_odometer()
# Output: This car has traveled 0 miles.