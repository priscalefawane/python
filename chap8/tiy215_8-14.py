def make_car(manufacture, model_name, **car_info):
    """Storing information about a car in a dictionary."""
    car_info['manufacture'] = manufacture.title()
    car_info['model_name'] = model_name.title()
    return car_info
car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True)
print(car)
my_car = make_car('kia', 'picanto',
                  color='green',
                  year=2018,
                  sun_roof=True)
print(my_car)