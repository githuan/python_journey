#!/usr/bin/env python3


prompt = "*** Mr. Wok Restaurant ***"
prompt += "\nHow many people are dining with us today? "

car = input(prompt)
car = int(car)

if car <=4:
    print(f"\tTable will be ready in 5 minutes.")
elif car <=7:
    print(f"\tTable will be ready in 10 minutes.")
else:
    print(f"\tTable will be ready in 15 minutes.")



