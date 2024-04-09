terms={
    'string':'A string is a group of characters',
    'integer':'An integer is a whole number',
    'dictionary':'A dictionary is a collection of key value pairs',
    'array':'An array is a collection of items',
    'tuple':'A tuple is a collection of items that cannot be modified'
}

for term in terms:
    print(f'{term.title()}: {terms[term]}\n')