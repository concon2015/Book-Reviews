def make_car(manufacturer, model, **features):
    car = {'manufacturer':manufacturer, 'model':model}
    for key, value in features.items():
        car[key]=value
    return car