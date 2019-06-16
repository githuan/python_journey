#!/usr/bin/env python3


def make_album(title, artist, year=None):
    """Return a dictionary of information about album."""
    album = {'title': title, 'artist': artist}
    if year:
        album['year'] = year
    return album


pop = make_album('hit me baby one more time', 'brittney spear', '1998')
print(pop)

rock = make_album('wind of change', 'scorpion', '1990')
print(rock)

soft = make_album('lady in red', 'chirs de burgh', '1986')
print(soft)

hard_rock = make_album('crazy train', 'ozzy osbourne')
print(hard_rock)

alt_metal = make_album('numb', 'linkin part')
print(alt_metal)
