# Chapter 2

## Variables
Assign variables using the equal sign `=` 

    Example: `variable_name = 'value'`

- Can only contain letters, numbers, and underscores
- Can only begin with letters and underscores
- Cannot use python keywords and function names
- Should be short but descriptive

## Strings
Data type in Python made up of characters. Could be a word or sentence

    Example: `string_variable = 'This is a string!'`

Can use methods to modify strings

- Title case `print(string_variable.title())`
- Lowercase `print(string_variable.lower())`
- Uppercase `print(string_variable.upper())`

Can use fstrings to insert text to strings

    Example: `greeting = f"Hello {first_name}! How are you today?"`

## Whitespace

Can add whitespace to strings with \t (tab) and \n (new line)

Can strip whitespace from strings

- Left strip `print(string_variable.lstrip())`
- Right strip `print(string_variable.rstrip())`
- Strip `print(string_variable.strip())`

Can remove prefixes and suffixes from strings

- Remove prefix `print(url_variable.removeprefix('http://'))`
- Remove suffix `print(url_variable.removeprefix('.html'))`

## Numbers

Integers are whole numbers (2, 4, 8)

Floats are numbers with decimal points (2.0, 4.7, 8.22)
    
- Dividing two integers or one integer and one float will return a float

## Mathematical Operations

- Add (`+`)
- Subtract(`-`)
- Divide (`/`)
- Multiply (`*`)
- Exponent (`**`)
- Modulus/Remainder (`%`)

## Multiple Assignment

`x, y, z = 1, 2, 3`

## Constants
Values that shouldn't change are called constants

Constants are variables that use all capital letters

Example: `MAX_CONNECTIONS = 4000`

## Comments
Comments are non executable portions of code use to explain things
Comments should be detailed and clear

Comments begin with the pound symbol (`#`)
Multi line comments begin and end with three double quotes (`"""`)

# Chapter 3

## Creating Lists
Create a list by assigning a variable with brackets

Example: `bicycles = ['trek', 'cannondale', 'redline', 'specialized']`

## Accessing Lists
Access an element of a list by using its index number

Example: `bicycles[0]`

- Lists begin at index position 0

## Adding, Removing, and Changing Lists

Change list items by assigning them like variables

Example: `bicycles[0] = 'huffy`

Append items to the end of a list using the .append() method

Example: `bicycles.append('huffy')`

Insert items to a list using the .insert() method

Example: `bicycles.insert(1, 'huffy')`

Delete items from a list using del by position

Example: `del bicycles[0]`

Remove an item from a list by position

Example: `bicycles.pop()` or `bicycles.pop(2)`

Remove an item from a list by value

Example: `bicycles.remove('huffy')`

- Will only remove the first instance. Need to use a loop to remove all instances.

## Sorting Lists

Can sort lists using the .sort() method

Example: `bicycles.sort()`

- This permanently changes the order of the list

Can sort lists temporarily with the function sorted()

Example: `print(sorted(bicycles))`

- This does not permanently change the order of the original list

Can reverse a list using the .reverse() method

Example: `bicycles.reverse()`

- This permanently changes the order of the list

## List Length

Can find length of a list using the len() function

Example: `len(bicycles)`

# Chapter 4

## Looping Through Lists
Iterate over items in a list via a `for` loop. 

- Remember to indent the line following the for statement
- Remember to end the for statement with a colon `:`

Example:

```
for item in items:
    print(item)
```

## Creating Numerical Lists

You can create a numerical list by using the `range` function

Example: `numbers = range(1,20)`

You can make the list skip numbers by incrementing the range function

Example: (odd numbers) `numbers = list(range(1,20,2))`

- Note: list() is needed around range to convert the range object into a list object

## Statistics With Lists

You can find the minimum, maximum, and sum for values in lists

```
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)
```

## List Comprehensions

You can initialize a list with values in one statement called a list comprehension

The format is `variable_name = [action for value in values]`

Example: `squares = [value**2 for value in range(1, 11)]`

## Slicing Lists

You can slice a list to only retrieve a subset of the list

Example: ```players = ['charles', 'martina', 'michael', 'florence', 'eli']; print(players[0:3])`

You can start at the beginning by omitting the first value

Example `players[:2]`

You can stop at the end by omitting the last value

Example `players[2:]`

- Note: This is useful for lists of unknown length

## Copying a List

You can copy a list by using a slice that has no start and stop position. Otherwise, the lists will be linked to eachother

Example: `friend_foods = my_foods[:]`

## Tuples

Tuples are a collection of items similar to a list but they use parenthesis `()` and cannot be modified after creation

- Note: Tuples can be overwritten but individual values cannot be changed.

Example: `dimensions = (200, 50)`

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

# Chapter 6

## Dictionaries

A dictionary is a collection of key value pairs

Example: `alien_0 = {'color': 'green', 'points': 5}`

## Accessing Dictionary Values

You can access dictionary values by using the key as an index

Example: `print(alien_0['color'])`

You can use the `get()` method to try and get a value and return a custom value if the key does not exist

Example: `point_value = alien_0.get('points', 'No point value assigned.')`

## Adding/Updating Key Value Pairs

You can add key value pairs by assigning a value to a key that does not exist. If the key does exist, the value will be updated

Example: `alien_0['x_position'] = 0`

## Removing Key Value Pairs

You can remove key value pairs from a dictionary with the `del` statement

Example: `del alien_0['color']`

## Looping Through Dictionaries

You can loop through dictionaries with a for loop and use either the key, value, or both.

Example: 
```
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

- The `items()` method will return all key value pairs.
- The `keys()` method will return all keys, however this is a implied default and can be left out.
- The `values()` method will return all values.

## Sorting Dictionaries

You can use the `sorted()` method to sort dictionaries

Example: 
```
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

## Dictionary Contents

A dictionary can contain many data types including strings, integers, tuples, lists, and even other dictionaries

Example:
```
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
```

```
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
        
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}
```

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

# Chapter 9

## Creating a Class

You can create a class with the `class` statement

Example:

```
class Dog:
"""A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
```

The `__init__()` method is used to initialize a instance. You must also pass the `self` parameter in the method

Here you can set default or initial values as needed

You can create multiple different instances of a class. This is meant to be used repeatably

## Creating a Class Instance

You can create a class by calling it similar to how you would a function

Example: `my_dog = Dog('Willie', 6)`

## Accessing Class Attributes

You can access attributes by using the class instance with dot notation for the variable/attribute

Example: `my_dog.name`

## Modifying Attribute Values

You can modify attribute values just as you would variables

Example: `my_dog.age += 1`

## Calling Class Methods

You can call methods on class instances that you previously defined

Example: `my_dog.sit()`

If the function supports it, you can pass values in the parenthesis

Example: `my_new_car.update_odometer(23)`

## Child Classes

You can make a child class that gets part of its configuration from a parent class

Example:
```
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
```

You must use the `super()` function to call a method from the parent class. This allows the child class to inherit the attributes from the parent class


## Importing Classes

You can import classes using the `import` keyword

Example: `from car import Car`

The first `car` is the name of the car.py file and the second `Car` is the name of the class within that file

You can import multiple classes or functions by separating them with commas

Example: `from car import Car, ElectricCar`

You can also import all classes from a module using the `*` wildcard

Example: `from module_name import *`

You can use aliases to make your modules easier to reference and avoid name collisions

Example: `from electric_car import ElectricCar as EC`

## Importing Modules

You can import an entire module by just using the `import` keyword

Example: `import car`

If you do this, you will need to use the `car` prefix before any classes or functions can be called from this module

Example: `my_mustang = car.Car('ford', 'mustang', 2024)`

# Chapter 11

## Installing Modules

Modules can be installed by using `pip` or `python -m pip`

Example: `python -m pip install pytest`

## Testing Functions

You can use pytest to test functions

 - Test files need to import the desired functions
 - Test files need to begin with 'test_'
 - Test functions need to begin with 'test_'
 - Test functions need to end with `assert value = 'expected result'`

 You can run pytest by running `python -m pytest` which will run all tests found within the current directory

Example:

 ```
from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
 ```

 ## Testing Classes

 You can create a fixture to build a class that is repeatable across multiple test functions

 You create a fixture by adding `@pytest.fixture` above the function that creates the class

 Following the class creation, you have to return the class and pass the name of the function as a parameter to each testing function

 Example:

 ```
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
 ```

 # Chapter 17

## Working with APIs

You can install the `requests` package to programmatically interact with websites and APIs

Example: `python -m pip install --user requests`

You can programmatically make web requests

Example:

```
import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()

# Process results.
print(response_dict.keys())
```