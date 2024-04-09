from city_functions import city_format

def test_city_format():
    output = city_format('santiago','chili')
    assert output == 'Santiago, Chili'

def test_city_format_population():
    output = city_format('santiago','chili',population=300000)
    assert output == 'Santiago, Chili - population 300000'
