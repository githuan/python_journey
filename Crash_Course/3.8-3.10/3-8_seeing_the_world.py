#!/usr/bin/env python3

wishlist_places = ['moscow, russia', 'helsinki, finland', 'dublin, ireland', 'prague, czech republic', 'kiev, ukraine']

print("The original list of places to visit:")
print(wishlist_places)

print("\n" + "Temporary sort without modifying the order of original list:")
print(sorted(wishlist_places))


print("\nThe original list of places to visit:")
print(wishlist_places)

print("\n" + "Temporary reverse without modifying the order of original list:")
print(sorted(wishlist_places, reverse=True))

print("\nThe original list of places to visit:")
print(wishlist_places)

print("\nReverse list:")
wishlist_places.reverse()
print(wishlist_places)

print("\nReverse list again to have the original list:")
wishlist_places.reverse()
print(wishlist_places)

print("\nSort order of list permanently:")
wishlist_places.sort()
print(wishlist_places)

print("\nReverse order of list permanently:")
wishlist_places.sort(reverse=True)
print(wishlist_places)
