#!/usr/bin/env python3


def make_car(manufacturer, model, **car_info):
    """Build a dictionary contain everything we know about a car."""
    car_info['manufacturer_name'] = manufacturer
    car_info['model_name'] = model
    return car_info


subaru = make_car('subaru',
                  'outback',
                  color='blue',
                  tow_package='True')
bmw_x5 = make_car('bmw',
                  'suv',
                  color='white',
                  engine='diesel',
                  sport_package='mSport')

print(subaru)
print(bmw_x5)
