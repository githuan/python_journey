#!/usr/bin/env python3

## Loop through a collection

for name in ['Christopher', 'Susan']: # Semicolon is required
    print(name) # All statements under for must be indented 4 spaces; just as if condition


## Looping a number of times

for index in range(0, 2): # will count up to 1 not 2
    print(index)


## Looping with a condition

names = ['Christopher', 'Susan']
index = 0
while index < len(names):
    print(names[index])
    # Change the condition!!
    index = index + 1