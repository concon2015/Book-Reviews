# Chapter 7

## User Input

You can receive user input with `input()`

Example: `name = input('What is your name? ')`

- Any string inside of the parenthesis will be a prompt given
- Leave a space at the end of prompts for formatting
- Input will be a string unless otherwise specified

## Modulo Operator

The modulo operator `%` is used to return remainders

Example: 
```
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
```

## While Loops

While loops can be used to indefinitely run code until the statement becomes false

Example:

```
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

You can allow the user to end a while loop by adding in a flag to quit

Example:

```
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```

You can exit a while loop by using the `break` statement

Example: 

```
while True:
    city = input(prompt)
    if city == 'quit':
        break
```

You can skip back to the beginning of a while loop using the `continue` statement

Example:

```
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```