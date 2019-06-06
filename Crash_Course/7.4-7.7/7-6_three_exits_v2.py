#!/usr/bin/env python3


prompt = "\nCreating your own pizza."
prompt += "\nPlease enter your topping: "

active = True
while active:
    topping = input(prompt)

    if topping == 'quit' or topping == 'q' or topping == 'exit' or topping == 'x':
        active = False
    else:
        print(f"{topping.title()} is added!")
