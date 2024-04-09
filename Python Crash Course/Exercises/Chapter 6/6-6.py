favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

names=['jen','rudder','phil','connor']

for name in names:
    if name in favorite_languages:
        print(f'Thank you for responding {name.title()}.')
    else:
        print(f'Please take the favorite language poll {name.title()}.')