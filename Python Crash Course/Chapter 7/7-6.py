active = True
while active:
    age = input('What is your age? ')
    if age != 'quit':
        if int(age) < 3:
            print("Your ticket is free.")
        elif int(age) < 13:
            print("Your ticket is $10")
        else:
            print('Your ticket is $15')
    else:
        active = False
        break
