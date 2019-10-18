#!/usr/bin/env python3

# Numbers can be stored in variables
pi = 3.14159
print(pi)

# You can do math with numbers
# + Addition
# - Subtraction
# * Multiplication
# / Division
# ** Exponent
first_num = 6
second_num = 2
print(first_num + second_num)
print(first_num ** second_num)

# If you combine strings with numbers, Python gets confused
days_in_feb = 28
# print(days_in_feb + ' days in February') # WRONG
# Correction - Convert number to string so Python will treat it as concatenate strings
print(str(days_in_feb) + ' days in February')

# Numbers can be stored as strings
# numbers stored as strings are treated as strings
first_num = '5'
second_num = '6'
print(first_num + second_num)

# The input function always returns strings
first_num = input('Enter first number ')
second_num = input('Enter second number ')
print(first_num + second_num)
# Numbers stored as strings must be converted to numeric values before doing math
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))
