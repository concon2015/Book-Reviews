from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print(randint(1,self.sides))
my_die = Die()
for i in range(int(input("Enter the number of rolls: "))):
    my_die.roll_die()