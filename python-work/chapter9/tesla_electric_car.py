import car as c

tesla1 = c.ElectricCar('tesla', 'model s', 2019)
print(tesla1.get_descriptive_name())
# Output: 2019 Tesla Model S

# tesla1.describe_battery()
# Output: This car has a 75-kWh battery.

tesla1.fill_gas_tank()
# Output: This car doesn't need a gas tank!

tesla1.battery.describe_battery()
# Output: This car has a 75-kWh battery.

tesla1.battery.get_range()
# Output: This car can go about 260 miles on a full charge!