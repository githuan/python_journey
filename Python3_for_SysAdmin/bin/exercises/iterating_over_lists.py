#!/usr/bin/env python3.7

# My third Python 3 for Administrator Exercise.

users = [{'admin': False, 'active': False, 'name': 'Jasmine'}, {'admin': False, 'active': True, 'name': 'Remi'}, {'admin': False, 'active': False, 'name': 'Ellyse'}, {'admin': True, 'active':True, 'name': 'Jayson'}]

line = 1

for user in users:
    prefix = f"{line} "

    if user['admin'] and user['active']:
        prefix += "Active - Admin "
    elif user['admin']:
        prefix += "Admin "
    elif user['active']:
        prefix += "Active "
    else:
        prefix += "Not an active user! "
    print(prefix + user['name'])
    line += 1
