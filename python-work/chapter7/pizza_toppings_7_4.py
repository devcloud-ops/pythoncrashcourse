# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'finish' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

prompt = "\nEnter pizza toppings you'd like to add to your pizza. "
prompt += "\nEnter a 'finish' when you are done!: "

topping = ''
toppings = []

while topping != 'finish':
    topping = input(prompt)
    toppings.append(topping)

print(f"\nI will add these toppings to your pizza: {toppings}")