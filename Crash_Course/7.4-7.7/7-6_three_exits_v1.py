#!/usr/bin/env python3


prompt = "\nCreating your own pizza."
prompt += "\nPlease enter your topping: "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"{message.title()} is added!")
