# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your 
# glossary.When you run your program again, these new words and meanings should
# automatically be included in the output.

python_glossary = {
    'dictionary': 'can store comma separated key value pairs',
    'list': 'can store searchable list of numbers, strings, and boolean values',
    'strings': 'can store text data',
    'booleans': 'can store true or false flags',
    'integers': 'can store numbers',
    'sets': 'look much similar to dictionaries because of curly braces',
    'for_loops': 'helps to go through each item in a list, dictionary & set',
    'list_comprehension': 'is a concise way of writing for loops',
    'if_elif_else_statment': 'helps with conditionals in a very structured way',
    'functions': 'a topic not understood yet'
}

# print(glossary_datatypes)
for k,v in python_glossary.items():
    print(f'A {k.capitalize()} {v}!')
