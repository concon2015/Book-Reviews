def make_car(manufacturer, model, **features):
    car = {'manufacturer':manufacturer, 'model':model}
    for key, value in features.items():
        car[key]=value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
my_old_accord = make_car('honda', 'accord', year=1991, color='white', headlights='popup')
print(my_old_accord)