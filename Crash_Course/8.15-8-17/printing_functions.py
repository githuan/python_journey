#!/usr/bin/env python3


def show_messages(messages):
    """Print each message in a list of messages."""
    for message in messages:
        msg = f"{message.capitalize()}"
        print(msg)
