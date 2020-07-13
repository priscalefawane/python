# Returning a value.
def city_country(city, country):
    """Return a string formatted like 'Santiago, Chile'."""
    return (f"{city.title()}, {country.title()}")

city = city_country('pretoria', 'south africa')
print(city)
city = city_country('gaborne', 'botswana')
print(city)
city = city_country('maseru', 'lesotho')
print(city)