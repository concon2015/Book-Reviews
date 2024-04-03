pets = [
    {
        'name':'rudder',
        'owner':'connor',
        'pet_type':'dog'
    },
    {
        'name':'ellie',
        'owner':'connor',
        'pet_type':'dog'
    },
    {
        'name':'leo',
        'owner':'clayton',
        'pet_type':'turtle'
    }
]

for pet in pets:
    for item in pet:
        print(pet)
        print(pets[pet][item])