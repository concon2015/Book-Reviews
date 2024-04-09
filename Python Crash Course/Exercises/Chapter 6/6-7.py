p1_information = {
    'first_name':'rudder',
    'last_name':'blackard',
    'age':5,
    'city':'burleson'
}

p2_information = {
    'first_name':'connor',
    'last_name':'blackard',
    'age':26,
    'city':'burleson'
}

p3_information = {
    'first_name':'ana',
    'last_name':'blackard',
    'age':27,
    'city':'burleson'
}

people= [p1_information,p2_information,p3_information]

for person in people:
    for key,value in person.items():
        print(key+':'+str(value))