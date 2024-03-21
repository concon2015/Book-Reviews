# Chapter 5

## If Statements

The `if` statement can be used to control program execution. Else can be used as a catch all statement

Example: 
```
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

If-Elif statements can be used to do multiple checks

- You can have multiple elif blocks
- The else statement is optional. Can be replaced with an elif for additional clarity

Example: 
```
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif cat =='audi':
        print(car.title())
    else:
        print('something else')
```

## Conditional Tests

You can check for equality with `==` two equal signs

Example: `car == 'bmw`

Make sure to use `lower()` to ignore case when necessary

Example: `car.lower() == 'bmw'`

You can check for inequality with `!=` an exclamation mark followed by an equal sign

Example: `car != 'ford'`

You can use use conditional tests to check numerical values `>`, `<`, `>=`, `<=`

Example: `number >= 42`

You can use the `and` and `or` statements to combine conditional tests

Example: `number > 42 and sky == 'blue'` or `number > 36 or sky == 'purple'`

## Check List Values

You can check if a value is in a list with `in` keyword

Example: `'mushrooms' in pizza_topping` or `'pepperoni' not in pizza_toppings`

You can check if a list is empty by using it as a conditional statement. If list is empty, the value will return False

Example: `if pizza_toppings`
