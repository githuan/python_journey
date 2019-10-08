#!/usr/bin/env python3

# String can be stored as variables
first_name = 'Christopher'
last_name = 'Harrison'

# You can combine strings with + sign
print(first_name + last_name)
print('Hello, ' + first_name + ' ' + last_name)

# You can use functions to modify strings
sentence = 'The dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.title())
print(sentence.count('a'))

# The functions help us formats strings we save to files and databasee, or display to users
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print('Hello, ' + first_name.capitalize() + ' ' \
    + last_name.capitalize())

# Custom string formatting
output = 'Hello, ' + first_name + ' ' + last_name
print(output.title())
output = 'Hello, {} {}'.format(first_name, last_name)
print(output.title())
output = 'Hello, {0} {1}'.format(first_name, last_name)
print(output.title())
# Only available in Python 3
output = f'Hello, {first_name} {last_name}'
print(output.title())