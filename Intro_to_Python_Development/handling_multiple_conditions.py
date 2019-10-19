#!/usr/bin/env python3

## When you use elif instead of multiple if statements,
## you can add a default action

get_province = input('What is your provice? ')
province = get_province.lower()
if province == 'alberta':
    tax = 0.05
elif province == 'nunavut':
    tax = 0.05
elif province == 'ontario':
    tax = 0.13
else: # This is the default action
    tax = 0.15


## If multiple conditions cause the same action,
## they can be combined into a single condition

if province == 'alberta' or province == 'nunavut': # combined into a single condition
    tax = 0.05
elif province == 'ontario':
    tax = 0.13
else:
    tax = 0.15


## If you have a list of possible values to check,
## you can use the "IN" operator

if province in('alberta', \
                'nunavut', \
                'yukon'): # Using "IN" operator
    tax = 0.05
elif province == 'ontario':
    tax = 0.13
else:
    tax = 0.15


## If an action depends on a combination of conditions,
## you can nest if statements

get_country = input('What country are you from? ')
country = get_country.lower()

if country == 'canada':
    if province in('alberta', \
                'nunavut', \
                'yukon'): # Using "IN" operator
        tax = 0.05
    elif province == 'ontario':
        tax = 0.13
    else:
        tax = 0.15

else:
    tax = 0.0
print(f'Your tax rate is: {tax}')