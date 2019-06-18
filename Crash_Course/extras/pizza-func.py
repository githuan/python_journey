#!/usr/bin/env python3


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping.capitalize()}")


make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
make_pizza('sausage', 'caramelized onion', 'fennel', 'scallion', 'grilled chicken')
make_pizza('thousand island dressing', 'cheddar cheese', 'sauerkraut', 'pastrami')
