#!/usr/bin/env python3


def make_sandwich(*sandwiches):
    """Summarize the sandwiches are a about to make."""
    print("\nMaking following sandwiches:")
    for sandwich in sandwiches:
        if sandwich == 'open-face vietnamese':
            print(f"\t- {sandwich.title()}")
        else:
            print(f"\t- {sandwich.capitalize()}")


make_sandwich('turkey breast')
make_sandwich('smoked ham', 'terryaki chicken')
make_sandwich('cheese steak', 'honey ham')
make_sandwich('omlette', 'grilled chicken', 'egg salad with avocado')
make_sandwich('roasted beef', 'open-face vietnamese', 'classic club')
