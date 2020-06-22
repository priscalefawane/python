glossary = {
    'variable': 'a storage address of information referred as value.',
    'immutable': 'values cannot be changed once they have been assigned.',
    'indentation': 'space between the edge of the editor and start of the code.',
    'string': 'anything inside quotes.',
    'float': 'any number with decimal point.',
    }
for k, v in glossary.items():
    print(f"\nkey: {k}")
    print(f"value: {v}")

# Automatically adding more terms to glossary.
print("current glossary is: ", glossary)

glossary['syntax'] = "a set of rules that defines how program will be written."
glossary['integers'] = 'positive or negative whole numbers with no decimal point.'
glossary['inequality'] = 'two items that does not have the same value.'
glossary['constant'] = 'type of variable that holds values which cannot change.'
glossary['comment'] = 'text that does not affect the outcome of a code.'
print("updated glossary is: ", glossary)

for k, v in glossary.items():
    print(f"\nkey: {k}")
    print(f"value: {v}")
