first_name = 'ada'
last_name = 'lovelace'
# Notice the f before the quotation marks. This f lets Python interpreter format the string to replace variable values.
full_name = f'{first_name} {last_name}'
print(full_name)
print(full_name.title())
print(full_name.capitalize())
print(full_name.casefold())
#print(full_name.center())
print(full_name.count('e'))
print(full_name.find('a'))
print(f"Hello, {full_name.title()}!")

#old formation
full_name2 = "{} {}".format(first_name, last_name)
print(full_name2)

#using tab whitespace
print("Faisal \t Siddiqui")
print("\tFaisal")

#using newline
print("Faisal is becoming a superhero in programming \n But he is impatient to learn things quickly... \n It will take time my friend.")
print("that new line \nchange worked!")
print("that new line \nchange worked! \n hello world!")
