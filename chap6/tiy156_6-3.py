# Using dictionary to make a glossary
glossary = {
    'variable': 'a storage address of information referred as value.',
    'immutable': 'values cannot be changed once they have been assigned.',
    'indentation': 'space between the edge of the editor and start of the code.',
    'string': 'anything inside quotes',
    'float': 'any number with decimal point.',
    }
for key, value in glossary.items():
    print(f"{key}: \n{value}\n")