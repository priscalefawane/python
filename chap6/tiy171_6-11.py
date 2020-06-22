# Using a dictionary in a dictionary
cities = {
    'johannesburg': {
        'country': 'south africa',
        'population': '5,783,000',
        'fact': 'the busiest airport in africa',
        },
    'bloemfontein': {
        'country': 'south africa',
        'population': '567,000',
        'fact': 'is the capital city of free state',
        },
    'durban': {
        'country': 'south africa',
        'population': '3,158,313',
        'fact': 'famous for being the busiest'
                ' port in south africa ',
        },
    }
for city, city_information in cities.items():
    print(f"\nCity: {city.title()}")
    population = city_information['population']
    fact = city_information['fact']

    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact.title()}.")