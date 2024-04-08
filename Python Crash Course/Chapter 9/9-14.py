from random import choice

#lottery_balls = ('1','2','3','4','5','6','7','8','9','10','a','b','c','d','e')
lottery_balls = ('a','b','c','d')

my_ticket = ['a','b','c','d']
draws = 0
active = True

winning_ticket = []
def draw_lottery():
    while len(winning_ticket) < 4:
        pulled_item = choice(lottery_balls)

        # Only add the pulled item to the winning ticket if it hasn't
        #   already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    print(winning_ticket)
    return winning_ticket

def check_ticket(ticket, winning_ticket):
    print('\n')    
    print(ticket)
    print(winning_ticket)
    print('\n')
    for i in ticket:
        if i not in winning_ticket:
            print(f'{i} not in {winning_ticket}')
    active=False

while active:
    check_ticket(my_ticket, draw_lottery())
    winning_ticket=[]
    draws += 1