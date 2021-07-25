number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

# The Modulo Operator in action
if number % 2 == 0:
    print(f"\n'{number}' is an even number.")
else:
    print(f"\n'{number}' is an odd number.")