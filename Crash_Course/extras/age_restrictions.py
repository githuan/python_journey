#!/usr/bin/env python3


age = input("How old are you? ")
age = int(age)

if age <= 17:
    print("\nYou will be able to vote when you are a little older.")
elif age <= 20:
    print("\nYou can vote but no tobaco of alcohol will be served.")
else:
    print("\nYou can party but do not drive under infulence.")
