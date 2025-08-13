from city_country import citycountry

def test_citycountry():
    city_name = citycountry('Santiago', 'Chile')
    assert city_name == 'Santiago,Chile'