# Making middle name optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted, middle_name is optional."""
    if middle_name: # This condition ensures that middle_name isn't empty
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# musician = get_formatted_name('jiMi', 'k.', 'hEnDrix')
musician = get_formatted_name('jiMi', 'hEnDrix')
print(musician)

print(get_formatted_name('muhammad','faiSal','siDDiqui'))