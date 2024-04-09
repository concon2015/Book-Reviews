sandwich_orders = ['rueben', 'pastrami','philly', 'pastrami' ,'pastrami', 'blt']
finished_sandwiches = []
print('We have ran out of pastrami!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Making {current_sandwich}.')
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f'I made a {sandwich}')