pizza_flavors = ['supreme', 'pepperoni', 'cheese']
for flavor in pizza_flavors:
    print(f'I like {flavor} pizza!')
print("I really like pizza!")

friend_pizzas = pizza_flavors[:]
friend_pizzas.append('buffalo chicken')

for flavor in friend_pizzas:
    print(f'My friend likes {flavor} pizza!')