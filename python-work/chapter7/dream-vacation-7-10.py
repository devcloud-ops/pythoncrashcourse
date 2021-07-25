# 7-10. Dream Vacation: Write a program that polls users about their dream 
# vacation. Write a prompt similar to If you could visit one place in the 
# world, where would you go? Include a block of code that prints the results 
# of the poll.

dream_vacation = {}
person = ''
location = ''
nextUser = 'y'

name = "Specify your name please?: "
poll = "If you could visit one place in the world, where would you go? "
next = "Is there another user to poll (y/n)? :"

# poll
while nextUser != 'n':
    person = input(name)
    location = input(poll)
    dream_vacation[person] = location
    nextUser = input(next)

# print(f"\n{dream_vacation}")

#results
print("\nHere are the results of the poll: ")
for p,l in dream_vacation.items():
    print(f"\t{p.title()} would like to visit {l.title()}.")