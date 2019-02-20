#!/usr/bin/env python3.7

# My second Python 3 for Administrator Exercise.

user = {'admin': True, 'active': False, 'name': 'Kevin'}
prefix = ""

if user['admin'] and user['active']:
    prefix = "ACTIVE - (ADMIN) "
elif user['admin']:
    prefix = "(ADMIN) "
elif user['active']:
    prefix = "ACTIVE - "

print(prefix + user['name'])
