#!/usr/bin/env python3


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jim', 'hendrix')
print(musician)

librarian = get_formatted_name('john', 'doe')
print(librarian)

cook = get_formatted_name('lea', 'sand')
print(cook)
