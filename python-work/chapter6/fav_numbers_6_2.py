# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a 
# favorite number for each person, and store each as a value in your 
# dictionary. Print each person’s name and their favorite number. For even 
# more fun, poll a few friends and get some actual data for your program.

fav_numbers = {
    'imran': 99,
    'kashif': 88,
    'ismail': 77,
    'alan': 66,
    'caroline': 55
}

imran_num = fav_numbers.get('imran')
kashif_num = fav_numbers.get('kashif')
ismail_num = fav_numbers.get('ismail')
alan_num = fav_numbers.get('alan')
caroline_num = fav_numbers.get('caroline')

print(f'\nImran\'s favorite number is: {imran_num}')
print(f'\nKashif\'s favorite number is: {kashif_num}')
print(f'\nIsmail\'s favorite number is: {ismail_num}')
print(f'\nAlan\'s favorite number is: {alan_num}')
print(f'\nCaroline\'s favorite number is: {caroline_num}')