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

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, flavors):
        super().__init__(name, cuisine)
        self.flavors = flavors
    def show_weekly_flavors(self):
        print(f'Our weekly flavors are:')
        for flavor in self.flavors:
            print(f'- {flavor.title()}')

restaurant = IceCreamStand('Scoops','Desert',['vanilla', 'chocolate', 'strawberry'])

restaurant.show_weekly_flavors()

