def build_profile(first, last, **my_info):
    """Building a dictionary containing things about me."""
    my_info['first_name'] = first.title()
    my_info['last_name'] = last.title()
    return my_info

my_profile = build_profile('prisca', 'lefawane',
                           gender='female',
                           location='tembisa',
                           age=33,
                           study='python', )
print(my_profile)