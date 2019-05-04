#!/usr/bin/env python3

precious = {
    'pet_name': 'precious',
    'owner': 'chris',
    'kind': 'yorkshire terrier',
    'color': 'brown',
    }

whiskey = {
    'pet_name': 'whiskey',
    'owner': 'chris',
    'kind': 'basenji',
    'color': 'black',
    }

sux = {
    'pet_name': 'sux',
    'owner': 'chris',
    'kind': 'wolfdog',
    'color': 'white',
    }

brian = {
    'pet_name': 'brian',
    'owner': 'chris',
    'kind': 'pug',
    'color': 'brown',
    }

moomoo = {
    'pet_name': 'moomoo',
    'owner': 'dad',
    'kind': 'american pitbull terrier',
    'color': 'white',
    }

spike = {
    'pet_name': 'spike',
    'owner': 'chris',
    'kind': 'american pitbull terrier',
    'color': 'black',
    }


pets = [
    precious, whiskey, sux, brian, moomoo, spike
    ]


for pet in pets:
    print("\nPet's Name: " + pet['pet_name'].title() +
          "\n\tOwner: " + pet['owner'].title() +
          "\n\tKind: " + pet['kind'].title() +
          "\n\tColor: " + pet['color'].title()
          )
