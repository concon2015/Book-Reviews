favorite_numbers = {
    'connor':[13,12],
    'ana':[1,2],
    'kennedy':[21,20],
    'rudder':[5,6],
    'ellie':[2,62]
}

for name in favorite_numbers:
    for i in favorite_numbers[name]:
            print(f'One of {name.title()}\'s favorite number are {i}')