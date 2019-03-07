#!/usr/bin/env python3

fruits = ['mango', 'watermelon', 'pineapple', 'grape', 'orange', 'apple', 'jackfruit' ,'kiwi' ,'banana', 'cranberries']

print("The first three kinds of fruits in the list are:")
for num in fruits[:3]:
    print(num.title())

print("\nThe middle four kinds of fruits in the list are:")
for num in fruits[-7:7]:
    print(num.title())

print("\nThe last three kinds of fruits in the list are:")
for num in fruits[-3:]:
    print(num.title())
