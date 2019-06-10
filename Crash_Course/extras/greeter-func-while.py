#!/usr/bin/env python3


def get_formatted_name(first_name, last_name, middle_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")

    f_name = input("First Name: ")
    if f_name == 'q':
        break


    l_name = input("Last Name: ")
    if l_name == 'q':
        break


    m_name = input("Middle Name: ")
    if m_name == 'q':
        break


    formatted_name = get_formatted_name(f_name, l_name, m_name)
    print(f"\nHello, {formatted_name}!")
