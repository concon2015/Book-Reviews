active = True
results={}
while active:
    name=input('What is your name? ')
    place=input('Where would you like to go? ')
    results[name]=place
    repeat = input('Would you like to poll anyone else? y/n ')
    if repeat == 'n':
        active = False

for name, place in results.items():
    print(f'{name.title()} would like to go to {place.title()}.')