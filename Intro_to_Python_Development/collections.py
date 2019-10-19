#!/usr/bin/env python3

## List are collections of items, using []
## can be any data type

names = ['Christopher', 'Susan']
print(names)


## You can start with an empty list

scores = []
scores.append(98) # Add new item to the end
scores.append(99)
print(scores)
print(scores[1]) # Collections are zero-indexed


## Arrays are also collections of items
## but specific to a type

from array import array # Add array library
scores = array('d') # Specify 'd' for digit. Check Python docs for Array
scores.append(96)
scores.append(97)
print(scores)
print(scores[1])

# The difference between arrays and list is
# array specify to one type of data in an array whereas
# list can be any data withn a list


## Common operations

names = ['Susan', 'Christopher']
print(len(names)) # Get the number of items
names.insert(0, 'Bill') # Insert before index
print(names)
names.sort()
print(names)


## Retrieving ranges

names = ['Susan', 'Christopher', 'Bill']
presenters = names[0:2] # Get the first two items
# Starting index and number of items to retrieve

print(names)
print(presenters)


## Dictionaries

person = {'first': 'Christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])