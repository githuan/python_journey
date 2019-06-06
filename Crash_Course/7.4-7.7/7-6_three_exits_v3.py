#!/usr/bin/env python3


prompt = "\nCreating your own pizza."
prompt += "\nPlease enter your topping: "

while True:
    topping = input(prompt)

    if topping == 'quit' or topping == 'q' or topping == 'exit' or topping == 'x':
        break
    else:
        print(f"{topping.title()} is added!")
