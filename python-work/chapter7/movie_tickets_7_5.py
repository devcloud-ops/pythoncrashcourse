# 7-5. Movie Tickets: A movie theater charges different ticket prices 
# depending on a person’s age. If a person is under the age of 3, the ticket
# is free; if they are between 3 and 12, the ticket is $10; and if they are 
# over age 12, the ticket is $15. Write a loop in which you ask users their 
# age, and then tell them the cost of their movie ticket.

prompt = "\nEnter the person age you'd like to buy tickets for. "
prompt += "\nEnter a 'finish' when you are done!: "
age = ''

while True:
    age = input(prompt)
    if age == 'finish':
        break
    else:
        age = int(age)
        if age < 3:
            print("\nThis person's ticket is free!")
        elif age >= 3 and age <= 12:
            print("\nThis person's ticket fare is $10")
        elif age > 12:
            print("\nThis person's ticket fare is $15")
