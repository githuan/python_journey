#!/usr/bin/env python3


prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit' or city == 'q' or city == 'exit' or city == 'x':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
