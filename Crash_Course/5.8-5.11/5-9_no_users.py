#!/usr/bin/env python3

#usernames = ['hotdogs', 'admin'] # For testing to validate "if" conditional.
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see today's status report?")
        else:
            print("Hello " + username.title() + ", thank you for logging in " +
                  "again.")
else:
    print("We need to add some users!")
