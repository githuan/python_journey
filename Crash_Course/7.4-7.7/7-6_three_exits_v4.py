#!/usr/bin/env python3


prompt = "\n--- Movie Ticketting System ---"
prompt += "\nPlease enter your age: "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        age = int(message)

        if age <= 3:
            print("\n\tYour movie entry is FREE!")
        elif age <= 12:
            print("\n\tYour movie entry cost is: $10")
        elif age >= 13:
            print("\n\tYour movie entry cost is: $15")
