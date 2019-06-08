#!/usr/bin/evn python3


print("\nMake T-shirts:")
def make_shirt(shirt_size, shirt_text):
    """Display shirt information."""
    print(f"\tCreated {shirt_size} T-shirt with message: {shirt_text.title()}")


make_shirt('large', 'i love N.Y.')
make_shirt(shirt_size='XL', shirt_text='beer')

