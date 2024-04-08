def describe_city(city,country='the United States'):
    print(f'{city.title()} is in {country.title()}.')

describe_city('Boston')
describe_city('cancun', country='mexico')
describe_city(city='barcelona',country="spain")