#!/usr/bin/env python3


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jim', 'hendrix')
print(musician)

librarian = get_formatted_name('john', 'doe', 'lee')
print(librarian)

cook = get_formatted_name('lea', 'sand', 'green')
print(cook)

electrician = get_formatted_name('aleksandr', 'mikhailov', 'anastasia')
print(electrician)

geometrist = get_formatted_name('ben', 'schmidt', 'becker')
print(geometrist)
