def describe_pet(animal_type, pet_name='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# with keyword_arguments, order of arguments doesn't matter
describe_pet(animal_type='hamster')
describe_pet(pet_name='kitty', animal_type='cat')
describe_pet('dog', 'willie')