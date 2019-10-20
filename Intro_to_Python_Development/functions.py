#!/usr/bin/env python3

### Functions
## Sometimes we copy and paste our code

#import datetime
## print timestamps to see how long sections of code take to run
#first_name = 'Susan'
#print('task completed')
#print(datetime.datetime.now())
#print()
#
#for x in range(0,10):
#    print(x)
#print('task completed')
#print(datetime.datetime.now())
#print()


## Use functions instead of repeating code

# Import the datetime class from datetime library
from datetime import datetime
# Print the current time
def print_time():
    print('task completed')
    # Now we don't need the extra datetime prefix
    print(datetime.now())
    print()

first_name = 'Susan'
print_time()

for x in range(0,10):
    print(x)
print_time()


## Pass the task name as a parameter

# Print the current time and task name
def print_time2(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name2 = 'Susan'
print_time2('first name assigned')

for x in range(0,10):
    print(x)
print_time2('loop completed')


## Another example, code looks different but same logic over and over

first_name3 = input('Enter your first name: ')
first_name3_initial = first_name3[0:1]
last_name3 = input('Enter your last name: ')
last_name3_initial = last_name3[0:1]

print(f'Your initials are: {first_name3_initial}{last_name3_initial}')


## We can still us a function, but this time it returns a value
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name4 = input('Enter your first name: ')
last_name4 = input('Enter your last name: ')

#first_name4_initial = get_initial(first_name4)
#last_name4_initial = get_initial(last_name4)
#
#print(f'Your initials are: {first_name4_initial}{last_name4_initial}')

# Shorten the above codes
print(f'Your intials are: {get_initial(first_name4)}{get_initial(last_name4)}')