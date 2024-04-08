sandwich_orders = ['rueben', 'philly', 'blt']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Making {current_sandwich}.')
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f'I made a {sandwich}')