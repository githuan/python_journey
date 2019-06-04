#!/usr/bin/env python3

prompt = "\nTell me something, and I will repeat it back to you: "
prompt +=  "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit' or message == 'q' or message == 'exit' or message == 'x':
        active  = False
    else:
        print(message)
