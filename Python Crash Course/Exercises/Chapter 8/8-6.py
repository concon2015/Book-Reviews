def city_country(city,country):
    return (f'"{city.title()}, {country.title()}"')

print(city_country('santiago','chili'))
print(city_country('dallas','Texas'))
print(city_country(country='mexico',city='cancun'))