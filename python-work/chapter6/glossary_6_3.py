# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.

# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.

# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary_datatypes = {
    'dictionary': 'can store comma separated key value pairs',
    'list': 'can store searchable list of numbers, strings, and boolean values',
    'strings': 'can store text data',
    'booleans': 'can store true or false flags',
    'integers': 'can store numbers'
}

# print(glossary_datatypes)

dictionary = glossary_datatypes.get('dictionary')
list = glossary_datatypes.get('list')
strings = glossary_datatypes.get('strings')
booleans = glossary_datatypes.get('booleans')
integers = glossary_datatypes.get('integers')

print(f'A Dictionary {dictionary}')
print(f'A List {list}')
print(f'A String {strings}')
print(f'A Boolean {booleans}')
print(f'An Integer {integers}')