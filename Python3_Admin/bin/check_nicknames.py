#!/usr/bin/env python3.7
#title           :template.py
#description     :This is a header template for a python script.
#author          :Thuan Q Nguyen
#date            :20190118
#version         :0.1
#usage           :
#notes           :
#python_version  :3.7.2
#==============================================================================

def gather_firstname():
    firstname = input("What is your first name? ").lower().strip()
    return firstname

while True:
    firstname = gather_firstname()
    if firstname.startswith('t'):
        print(f"Your nickname is: Jayson")
        continue
    elif firstname.startswith('p'):
        print(f"Your nickname is: Jasmine")
        continue
    elif firstname.startswith('e'):
        print(f"Your nickname is: Tyti")
        continue
    elif firstname.startswith('r'):
        print(f"Your nickname is: Toto")
        continue
    else:
        print("Your name is not on the guess list.")
        x = input("Did you want to quit? ").lower().strip()
        if x.startswith('y'):
            print("Goodbye!")
            break
        if x.startswith('n'):
            continue
        else:
            print("Invalid choice, this program will restart.")
            continue
