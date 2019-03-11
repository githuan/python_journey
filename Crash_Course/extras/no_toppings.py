#!/usr/bin/env python3

requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

