# Dictionaries

alien_1 = {}
print(alien_1)

# Adding Alien's position on the screen:
alien_1['color'] = 'red'
alien_1['points'] = 15
alien_1['x_position'] = 0
alien_1['y_position'] = 45

print('old alient dictionary values:')
print(alien_1)

# Alien changing color
alien_1['color'] = 'yellow'
print('new alient dictionary values:')
print(alien_1)

# Alient speed key-value
alien_1['speed'] = 'medium'
print(alien_1)

# Print Origin position of the alien
print(f"Original position: {alien_1['x_position']}")


# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if (alien_1['speed'] == 'slow'):
    x_increment = 1
elif (alien_1['speed'] == 'medium'):
    x_increment = 2
else:
    # this must be a fallen alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_1['x_position'] = alien_1['x_position'] + x_increment

print(f"New position: {alien_1['x_position']}")