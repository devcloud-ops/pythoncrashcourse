# Slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f'All players in this list: {players}')
# Output: ['charles', 'martina', 'michael', 'florence', 'eli']

# Slice the players list by giving me on first 3 members
print(players[0:3])
# Output: ['charles', 'martina', 'michael']

# Slice the players list by giving me members from index 1 through 4.
print(players[1:4])
# Output: ['martina', 'michael', 'florence']

# Slice the players list by giving me all members from index 0 through 4.
print(players[:4])
# Output: ['charles', 'martina', 'michael', 'florence']

# Slice the players list by giving me all members from index 2 through end of the list.
print(players[2:])
# Output: ['michael', 'florence', 'eli']

# Recall that a negative index returns an element a certain distance from the end of a list;therefore, you can output any slice from the end of a list. For example, if
# we want to output the last three players on the roster, we can use the slice players[-3:]:
# Output the last three players on the roster
print(players[-3:])


# You can include a third value in the brackets indicating a slice. If a third value is
# included, this tells Python how many items to skip between items in the specified range.
cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
print(cubes[1:6:2])
# Output: [8, 64, 216]