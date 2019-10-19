#!/usr/bin/env python3

## Sometimes you can combine conditions with "AND" instead of nesting if statements

get_gpa = input('What is your GPA? ')
get_grade = input('What is your grade? ')
gpa = float(get_gpa)
lowest_grade = float(get_grade)

if gpa >= .85:
    if lowest_grade >= .70:
        print('Well done!')

if gpa >= .85 and lowest_grade >= .70:
    print('Well done!!')


## If you need to remember the result of a condition check later in your code,
## use Boolean variables as flags

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

# Somewhere later in your code
if honour_roll: # Actually honour_roll = True but this is how Python understand
    print("You're on Honour Roll!")