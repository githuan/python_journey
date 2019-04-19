#!/usr/bin/env python3


# Store info about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'peperoni'],
    }


# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
