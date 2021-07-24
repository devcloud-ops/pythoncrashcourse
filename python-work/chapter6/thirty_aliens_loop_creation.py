aliens = []

# Make 30 green aliens.
for number_of_alien in range(30):
    number_of_alien = {'color': 'green', 'points':5, 'speed': 'slow'}
    aliens.append(number_of_alien)

# Show how many aliens were created.
print(f"Total number of aliens created: {len(aliens)}")

print("Before change...")

for alien in aliens[:5]:
    print(alien)

# Changing first 3 aliens to green:
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

print("...")
print("After change...")


for alien in aliens[:5]:
    print(alien)

# Output:
# Total number of aliens created: 30
# Before change...
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# ...
# After change...
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}