#!/usr/bin/env python3


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping.capitalize()}")


make_pizza(12, 'peperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza(18, 'sausage', 'caramelized onion', 'fennel', 'scallion', 'grilled chicken')
make_pizza(18, 'thousand island dressing', 'cheddar cheese', 'sauerkraut', 'pastrami')
