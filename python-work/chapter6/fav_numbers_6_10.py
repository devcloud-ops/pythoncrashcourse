# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
# so each person can have more than one favorite number. Then print each 
# person’s name along with their favorite numbers.

fav_numbers = {
    'imran': [99,999,9999],
    'kashif': [88,888,8888,88888],
    'ismail': [77,777],
    'alan': [66,666,6666,66666,666666],
    'caroline': [55,555,5555],
}

for person,numbers in fav_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")