#!/usr/bin/env python3

## We often need current date and time when logging errors and saving data
# To get current date and time,
# we need to use the datetime library
from datetime import datetime, timedelta

current_date = datetime.now()
# The now function ".now()" returns a datetime object
print('Today is: ' + str(current_date))


## There are functions you can use with datetime objects to manipulate dates
today = datetime.now()
print('Today is: ' + str(today))

# timedelta function is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))


## Use date functions to control date formatting
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))


## Sometimes you recieve the date as a string,
# and need to convert it to a datetime object
birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print(f'Birthday: {str(birthday_date)}')


## Converting it to a datetime allows you to use the date functions
birthday_eve = birthday_date - one_day
print(f'Day before birthday: {str(birthday_eve)}')


## Make sure you add exception handling in case the date entered is invalid