#!/usr/bin/env python3


def greet_users(names):
    """Print a simkple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['bob', 'alex', 'tim', 'joe', 'rachel', 'ejz', 'tom', 'kovis'
             , 'ellen', 'whitney']
greet_users(usernames)
