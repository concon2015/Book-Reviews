class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    def describe_restaurant(self):
        print(f'Welcome to {self.name} where we serve {self.cuisine.title()} food!')
    def open_restaurant(self):
        print('The restaurant is open!')

my_restaurant = Restaurant('Dominos','italian')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
