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