# Chapter 10

# Opening with Files

You can work with files using the `pathlib` library

You can open a file using the `Path()` function

Example: `path = Path('file.txt')`

You can check if a file exists by using the `exists()` method

Example: `path.exists()`

## Reading Files

You can read content from a file using the `read_text()` method. This reads all text into a single string

Example: `content = path.read_text()`

You can split a file into an array with each line by using the `splitlines()` function

Example: `lines = content.splitlines()`

## Writing Files

You can write to files using the `write_text()` function. 

Example: `path.write_text('This is writing to a file!')`

`write_text()` will overwrite all existing content in the file. To write multiple lines, consolidate them into one string object and write all at once

Example: 

```
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)
```

## Exceptions

You can handle exceptions using `try-except` blocks

Example:

```
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

It is optional to name the type of error in the except block but it allows you to be more granular with error messages

You can fail silently by using the `pass` statement in an `except` block

Example:

```
except FileNotFoundError:
    pass
```

## Working with JSON Data

You can use the `json` library to work with JSON files

You can output python variables and data into json with `json.dumps`

Example: `contents = json.dumps(numbers)`

You can import json data into python with `json.loads`

Example: `numbers = json.loads(contents)`