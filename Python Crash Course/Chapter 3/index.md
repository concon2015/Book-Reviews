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