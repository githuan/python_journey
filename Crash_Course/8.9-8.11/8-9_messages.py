#!/usr/bin/env python3


def show_messages(messages):
    """Print each message in a list of messages."""
    for message in messages:
        msg = f"{message.capitalize()}"
        print(msg)


all_msg = ["life is what happens when you're busy making other plans."
           ,'you only live once, but if you do it right, once is enough.'
           ,'the only impossible journey is the one you never begin.'
           ,"if you aren't going all the way, why go at all?"
           ,"life would be tragic if it wren't funny."]
show_messages(all_msg)
