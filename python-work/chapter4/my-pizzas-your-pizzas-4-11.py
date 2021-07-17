# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.

my_pizzas = ['chicken','pepperoni','chicken_bbq', 'chicken_tikka']
friend_pizzas = my_pizzas[:]

my_pizzas.append('margherita')
friend_pizzas.append('chicken_supreme')

print(f'\nMy list of pizzas are: {my_pizzas}')
print(f'\nMy friend\'s list of pizzas are: {friend_pizzas}')

for pizza in my_pizzas:
    print(f'\nMy favorite pizzas are: {pizza.title()}')

for pizza in friend_pizzas:
    print(f'\nMy friend\'s favorite pizzas are: {pizza.title()}')
