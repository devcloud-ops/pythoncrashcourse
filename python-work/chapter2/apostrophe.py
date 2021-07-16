#Testing apostrophe inside a string

# This works without issue because double quotes were used
message = "One of Python's strenths is its diverse community!"
print(message)

# This errors out because single quotes were used:
message = 'One of Python\'s strenths is its diverse community!'
print(message)