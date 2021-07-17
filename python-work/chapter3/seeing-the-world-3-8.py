# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its order has changed.
# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

# • Store the locations in a list. Make sure the list is not in alphabetical order.
locations = ['USA','UAE','EU','CHINA','UK']



# • Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
print(f'\nI would like to visit these places in the world: {locations}\n')
# output: I would like to visit these places in the world: ['USA', 'UAE', 'EU', 'CHINA', 'UK']


# • Use sorted() to print your list in alphabetical order without modifying the actual list.
print(f'Here is a sorted list of locations that I would like to visit in alphabetical order: {sorted(locations)}\n')
# output: Here is a sorted list of locations that I would like to visit in alphabetical order: ['CHINA', 'EU', 'UAE', 'UK', 'USA']


# • Show that your list is still in its original order by printing it.
print(f'The list of locations I would like to visit are still in their original order: {locations}\n')
# output: The list of locations I would like to visit are still in their original order: ['USA', 'UAE', 'EU', 'CHINA', 'UK']


# • Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(f'Here is a sorted list of locations that I would like to visit in reverse alphabetical order: {sorted(locations, reverse=True)}\n')
# output: Here is a sorted list of locations that I would like to visit in reverse alphabetical order: ['USA', 'UK', 'UAE', 'EU', 'CHINA']


# • Show that your list is still in its original order by printing it.
print(f'The list of locations I would like to visit are still in their original order: {locations}\n')
# output: The list of locations I would like to visit are still in their original order: ['USA', 'UAE', 'EU', 'CHINA', 'UK']


# • Use reverse() to change the order of your list. Print the list to show that its order has changed.
locations.reverse()
print(f'Here is a sorted list of locations that I would like to visit in reverse order: {locations}\n')
# output: Here is a sorted list of locations that I would like to visit in reverse order: ['UK', 'CHINA', 'EU', 'UAE', 'USA']


# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
locations.reverse()
print(f'The list of locations I would like to visit are still in their original order: {locations}\n')
# output: The list of locations I would like to visit are still in their original order: ['USA', 'UAE', 'EU', 'CHINA', 'UK']


# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
locations.sort()
print(f'Here is a sorted list of locations that I would like to visit in alphabetical order: {locations}\n')
# output: Here is a sorted list of locations that I would like to visit in alphabetical order: ['CHINA', 'EU', 'UAE', 'UK', 'USA']


# • Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
locations.sort(reverse=True)
print(f'Here is a sorted list of locations that I would like to visit in reverse alphabetical order: {locations}\n')
# output: Here is a sorted list of locations that I would like to visit in reverse alphabetical order: ['USA', 'UK', 'UAE', 'EU', 'CHINA']