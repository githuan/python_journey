#!/usr/bin/env python3


prompt = "\n--- Movie Ticketting System ---"
prompt += "\nPlease enter your age: "

active = True
while active:
    user_input = input(prompt)

    if user_input == 'quit' or user_input == 'q' or user_input == 'exit' \
            or user_input == 'x':
       active = False 

    else:
        age = int(user_input)
        
        if age <= 3:
            print("\n\tYour movie entry is FREE!")
        elif age <= 12:
            print("\n\tYour movie entry cost is: $10")
        else:
            print("\n\tYour movie entry cost is: $15")
