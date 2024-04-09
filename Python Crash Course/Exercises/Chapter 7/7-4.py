active = True
toppings=[]
while True:
    topping=input('Enter pizza toppings. Type quit to exit. ')
    if topping=='quit':
        break
    else:
        toppings+=topping
        print(f'Adding {topping} to your pizza.')
    