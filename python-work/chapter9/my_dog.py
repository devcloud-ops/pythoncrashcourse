import dog as d

#################################################
print("\n\n")
#################################################

# 1st instantiation of dog
my_dog = d.Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")

my_dog.sit()
my_dog.roll_over()

#################################################
print("\n\n")
#################################################

# Second instantiation of dog
my_dog2 = d.Dog('Kim', 12)

print(f"My dog's name is {my_dog2.name}.")
print(f"My dog's age is {my_dog2.age}.")

my_dog2.sit()
my_dog2.roll_over()