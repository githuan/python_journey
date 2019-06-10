#!/usr/bin/env python3


def print_msg(send_messages, sent_messages):
    """
    Simulate printing each message, until none left.
    Move each message to sent_messages after printing.
    """
    while send_messages:
        current_message = send_messages.pop()
        print(f"Quote: {current_message.capitalize()}")
        sent_messages.append(current_message)


def show_sent_msg(sent_messages):
    """Show all messages that were printed."""
    print("\nThe following messages have been printed:")
    for sent_message in sent_messages:
        print(f"\t{sent_message.capitalize()}")

orig_messages = ["life is what happens when you're busy making other plans."
                ,'you only live once, but if you do it right, once is enough.'
                ,'the only impossible journey is the one you never begin.'
                ,"if you aren't going all the way, why go at all?"
                ,"life would be tragic if it wren't funny."]
send_messages = orig_messages[:]
sent_messages = []


print_msg(send_messages, sent_messages)
show_sent_msg(sent_messages)
show_sent_msg(orig_messages)
