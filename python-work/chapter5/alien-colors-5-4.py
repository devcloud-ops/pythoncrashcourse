# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
# and write an if-else chain.
# • If the alien’s color is green, print a statement that the player just 
# earned 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just 
# earned 10 points.
# • Write one version of this program that runs the if block and another that
# runs the else block.

# version 1
# alien_color = 'green'

# version 2
alien_color = 'yellow'

if (alien_color == 'green'):
    points_earned = 5
    statement = ' '.join(("\nCongratulations, you just shot down a green", 
                          f"alien and earned {points_earned} points!"))
    print(statement)
elif (alien_color != 'green'):
    points_earned = 10
    statement = ' '.join(("\nCongratulations, you just shot down a non-green", 
                          f"alien and earned {points_earned} points!"))
    print(statement)