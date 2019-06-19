#!/usr/bin/env python3
## Importing 5 functions


import show_messages as sm
from make_car import make_car as mc
from build_profile import build_profile as bp
import make_sandwich as msw
from make_pizza import *

## Show message part
all_msg = ["life is what happens when you're busy making other plans."
           ,'you only live once, but if you do it right, once is enough.'
           ,'the only impossible journey is the one you never begin.'
           ,"if you aren't going all the way, why go at all?"
           ,"life would be tragic if it wren't funny."]
sm.show_messages(all_msg)


## Make car part
print("\n\n")

subaru = mc('subaru',
                  'outback',
                  color='blue',
                  tow_package='True')
bmw_x5 = mc('bmw',
                  'suv',
                  color='white',
                  engine='diesel',
                  sport_package='mSport')

print(subaru)
print(bmw_x5)


## Build profile part
print("\n\n")

my_profile = bp('thuan',
                           'nguyen',
                           state='new york',
                           town='middletown',
                           county='orange'
                           )

print(my_profile)


## Make sandwich part
print("\n\n")

msw.make_sandwich('turkey breast')
msw.make_sandwich('smoked ham', 'terryaki chicken')
msw.make_sandwich('cheese steak', 'honey ham')
msw.make_sandwich('omlette', 'grilled chicken', 'egg salad with avocado')
msw.make_sandwich('roasted beef', 'open-face vietnamese', 'classic club')


## Make pizza part
print("\n\n")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
