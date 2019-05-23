#!/usr/bin/env python3


friend_fav_nums = {
    'anna': ['28', '35', '44'],
    'mathew': ['33', '88', '99'],
    'borjorn': ['21', '01', '07', '22'],
    'levis': ['14', '06', '13'],
    'brook': ['54', '12', '16', '81', '00', '77'],
    }


for name, numbers in friend_fav_nums.items():
    print("\n" + name.title() + "'s favorite numbers are:")

    for number in sorted(numbers):
        print("\t" + number)
