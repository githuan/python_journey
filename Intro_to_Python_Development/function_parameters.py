#!/usr/bin/env python3

## Functions can accept multiple parameters,
## just remember to pass the agruments in
## the same order they are listed in the
## function declaration

def get_initial(name, force_uppercase): # Multiple parameters
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name, False) # Pass agruments in the same order

print(f'Your initial is: {first_name_initial}')


## You can specify a default value for a parameter

def get_initial2(name, force_uppercase=False): # Set default paramenter value
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

last_name = input('Enter your last name: ')
last_name_initial = get_initial2(last_name)

print(f'Your initial is: {last_name_initial}')