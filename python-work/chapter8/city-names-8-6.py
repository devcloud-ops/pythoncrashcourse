# 8-6. City Names: Write a function called city_country() that takes in the 
# name of a city and its country. The function should return a string formatted
# like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.

def city_country(city,country):
    """This function returns formatted string"""
    formatted_str = "_________________________________________________"
    formatted_str += f"\n{city.title()}, {country.title()}\n"
    formatted_str += "_________________________________________________\n"
    return formatted_str

city1 = city_country('melbourne','australia')
city2 = city_country('sydney','australia')
city3 = city_country('dubai','united arab emirates')

print(city1)
print(city2)
print(city3)