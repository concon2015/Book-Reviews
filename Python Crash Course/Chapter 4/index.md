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