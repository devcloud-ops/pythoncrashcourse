# Using continue statement
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # the continue statement tells Python to ignore the rest of
                 # the loop and return to the beginning, hence not printing #
    print(current_number)
