def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# default value expected for second argument
describe_pet(pet_name='hamster') 

# with keyword_arguments, order of arguments doesn't matter
describe_pet(pet_name='kitty', animal_type='cat')

# positional arguments provided
describe_pet('willie','dog')