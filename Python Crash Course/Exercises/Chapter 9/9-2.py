class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    def describe_restaurant(self):
        print(f'Welcome to {self.name} where we serve {self.cuisine.title()} food!')
    def open_restaurant(self):
        print('The restaurant is open!')

my_restaurant1 = Restaurant('Dominos','italian')
my_restaurant2 = Restaurant('Chilis','family')
my_restaurant3 = Restaurant('Subway','sandwiches')
my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()