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