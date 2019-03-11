#!/usr/bin/env python3

usernames = ['sam smith', 'ashley brown', 'mark jorge', 'susan clark',
             'haley martin', 'admin', 'long lee', 'michael moore',
             'ariel anderson', 'thanh nguyen']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see today's status report?")
    else:
        print("Hello " + username.title() + ", thank you for logging in again.")
