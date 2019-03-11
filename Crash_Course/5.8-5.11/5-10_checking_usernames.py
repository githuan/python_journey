#!/usr/bin/env python3

current_users = ['South Martin', 'Jeeve Brown', 'admin', 'Minh Nguyen',
                 'Long Lee']

new_users = ['Ashley Black', 'Lenny Jones', 'Angelina Garcia', 'South Martin',
             'Minh Nguyen']

for new_user in new_users:
    if new_user in current_users:
        print(new_user + " is existed! Please choose another username.")
    else:
        print(new_user + " is available.")
