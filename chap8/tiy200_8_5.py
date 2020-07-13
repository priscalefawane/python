# Default value and equivalent function calls
def describe_city(name, country='south africa'):
    """Display a city information"""
    print(f"{name.title()} is in {country.title()}.")

describe_city('cape town')
describe_city('pretoria')
describe_city('gaborone', 'botswana')
