#!/usr/bin/env python3

# Empty dictionary then append to it
christopher = {}
christopher['first'] = 'Christopher'
christopher['last'] = 'Harrison'

# A filled dictionary, could also be appended
susan = {'first': 'Susan', 'last': 'Ibach'}

# Pull dictionaries in as a list
people = [christopher, susan]
# Add Mr. Gates to the list
people.append({';first': 'Bill', 'last': 'Gates'})
# Get presenters
presenters = people[0:2] # New list is created, original is intact.
print(len(presenters)) # len function doest not use index.
print()
print(presenters)
print()
print(people)