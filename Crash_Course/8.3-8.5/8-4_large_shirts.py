#!/usr/bin/evn python3


print("\nMake Large shirts:")
def make_shirt(shirt_text, shirt_size='large'):
    """Display shirt information."""
    print(f"\tCreated {shirt_size} T-shirt with message: {shirt_text.title()}")


make_shirt('i love python')
make_shirt(shirt_size='L', shirt_text='daytona')
make_shirt(shirt_size='M', shirt_text='daytona')
make_shirt(shirt_size='S', shirt_text='i love coding')

