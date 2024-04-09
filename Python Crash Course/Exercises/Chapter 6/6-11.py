cities = {
    'dallas' : {
        'country':'united states',
        'population': 300000,
        'food':'bbq'
    },
    'tokyo' : {
        'country':'japan',
        'population': 3000000,
        'food':'sushi'
    },
    'florida' : {
        'country':'united states',
        'population': 200000,
        'food':'seafood'
    }
}
for city, city_info in cities.items():
    print(f'{city.title()} in in {city_info['country'].title()}')
    print(f'{city.title()}\'s population is {city_info['population']}')
    print(f'{city.title()}\'s best food is {city_info['food']}')
