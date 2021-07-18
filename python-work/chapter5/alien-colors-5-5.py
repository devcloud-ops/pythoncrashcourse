# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an 
# if-elif-else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

# version 1
# alien_color = 'green'

# version 2
# alien_color = 'yellow'

# version 3
alien_color = 'red'


if (alien_color == 'green'):
    points_earned = 5
    statement = ' '.join(("\nCongratulations, you just shot down a green", 
                          f"alien and earned {points_earned} points!"))
    print(statement)
elif (alien_color == 'yellow'):
    points_earned = 10
    statement = ' '.join(("\nCongratulations, you just shot down a yellow", 
                          f"alien and earned {points_earned} points!"))
    print(statement)
elif (alien_color == 'red'):
    points_earned = 15
    statement = ' '.join(("\nCongratulations, you just shot down a red", 
                          f"alien and earned {points_earned} points!"))
    print(statement)