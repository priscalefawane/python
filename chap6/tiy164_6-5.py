# Three major rivers and the country each river runs through
major_rivers = {
    'mississippi': 'united state',
    'zambezi': 'mozambique',
    'amazon': 'brazil',
    }
for key, value in major_rivers.items():
    print(f"\nThe {key.title()} runs through {value.title()}.")
    print(key.title())
    print(value.title())
