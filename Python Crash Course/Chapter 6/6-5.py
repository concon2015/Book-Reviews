rivers = {
    'nile':'egypt',
    'rio grande':'texas',
    'amazon':'brazil'
}

for river, country in rivers.items():
    print(f'The {river} runs through {country}.')

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)