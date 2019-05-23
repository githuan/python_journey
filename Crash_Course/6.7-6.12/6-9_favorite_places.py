#!/usr/bin/env python3


favorite_places = {
    'ngan': ['dubai', 'saigon', 'da nang'],
    'me': ['us', 'saigon', 'da nang', 'ukraine', 'russia', 'czech', 'ireland', 'swissland', 'georgia', 'belarus'],
    'allysa': ['grand cayon', 'california', 'arizona'],
    'mike': ['ukraine', 'russia', 'german'],
    'jasmine': ['us', 'saigon', 'europe countries'],
    }


for person, places in  favorite_places.items():
    if person == 'me':
        print("\nMy favorite places are:")
    else:
        print("\n" + person.title() + "'s favorite places are:")

    for place in places:
        if place == 'us':
            print("\tUS")
        else: 
            print("\t" + place.title())
