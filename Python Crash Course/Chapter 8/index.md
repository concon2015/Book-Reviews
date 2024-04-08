# Chapter 8

## Functions

You can define functions to use code in a repeatable way with the `def` statement

Example:
```
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
```

## Arguments

You can pass parameters/arguments in with the function. You can also define default values in the function declaration

Example: `def describe_pet(pet_name, animal_type='dog'):`

You can pass arguments in based on position or based on value

Example: `describe_pet(pet_name='rudder',animal_type='cat')`

You can make arguments optional by passing a empty string as the default value

Example: `def get_formatted_name(first_name, last_name, middle_name=''):`

You can pass an arbitrary number of arguments by adding a single asterisk in the function declaration

Example: `def make_pizza(*toppings):`

You can pass an arbitrary number of key value pairs by adding two asterisks in the function declaration

Example: 
```
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')

def build_profile(first, last, **user_info):
```


## Returning Values

You can return data from a function with the `return` keyword

Example:

```
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
```

- You can return any data type (string, integer, dictionary, list, tuple, boolean, etc.)


## Modules

You can import other functions from other python files, called modules, by using the `import` keyword

Example:

```
import pizza

pizza.make_pizza(16, 'pepperoni')
```

You can also import specific functions

Example:  `from module_name import function_name, function_name2`

You can give a function an alias

Example: `from pizza import make_pizza as mp`

You can also import all functions from a module

Example: `from pizza import *`