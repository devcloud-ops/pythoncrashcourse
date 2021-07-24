# 6-11. Cities: Make a dictionary called cities. Use the names of three 
# cities as keys in your dictionary. Create a dictionary of information about 
# each city and include the country that the city is in, its approximate 
# population, and one fact about that city. The keys for each city’s dictionary 
# should be something like country, population, and fact. Print the name of 
# each city and all of the information you have stored about it.

cities = {
    'melbourne': {
        'country': 'australia',
        'population': 5061439,
        'fact': 'has the fourth largest tram system in the world overall!'
        },
    'dubai': {
        'country': 'united arab emirates',
        'population': 2921376,
        'fact': 'has a museum dedicated to coffee!'
        },
    'dhahran': {
        'country': 'kingdom of saudi arabia',
        'population': 240742,
        'fact': 'hosts head quarters of world\'s largest oil producer: Aramco!'
        },
}

for city,details in cities.items():
    print(f"\n{city.title()} statistics are as follows:")
    print(f"\tIs located in: {details['country'].title()}")
    print(f"\tHas population, as of 2021: {details['population']}")
    print(f"\tFact include: {details['fact']}")