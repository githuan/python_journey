#!/usr/bin/env python3.7

# Input function


name = input("What is your name? ")
dob = input("What is your date of birth? ")
age = int(input("How old are you? "))

print(f"{name} was born on {dob}")
print(f"Half of your age is {int(age / 2)}")
