aliens = []

# Make 30 green aliens.
for number_of_alien in range(30):
    number_of_alien = {'color': 'green', 'points':5, 'speed': 'slow'}
    aliens.append(number_of_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens were created
print(f"Total number of aliens created: {len(aliens)}")