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

