#!/usr/bin/env python3


prompt = "Enter a number, I will tell if it is a multiple of ten: "

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(f"\tFabulous! {number} is a multiple of ten.")
else:
    print(f"\t{number} is not a multple of ten.")
