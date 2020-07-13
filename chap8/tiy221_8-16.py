import pets

pets.describe_pet('hamster', 'harry')
pets.describe_pet('dog', 'willie')

from pets import describe_pet

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


from pets import describe_pet as dp

dp('hamster', 'harry')
dp('dog', 'willie')


import pets as p

p.describe_pet('hamster', 'harry')
p.describe_pet('dog', 'willie')


from pets import *

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')







