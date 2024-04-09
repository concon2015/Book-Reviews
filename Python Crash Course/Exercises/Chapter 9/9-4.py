class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    def describe_restaurant(self):
        print(f'Welcome to {self.name} where we serve {self.cuisine.title()} food!')
    def open_restaurant(self):
        print('The restaurant is open!')
    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant('Dominos','italian')

print(restaurant.number_served)
restaurant.number_served = 15
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)

