#!/usr/bin/env python3


def make_sandwich(*sandwiches):
    """Summarize the sandwiches are a about to make."""
    print("\nMaking following sandwiches:")
    for sandwich in sandwiches:
        if sandwich == 'open-face vietnamese':
            print(f"\t- {sandwich.title()}")
        else:
            print(f"\t- {sandwich.capitalize()}")

