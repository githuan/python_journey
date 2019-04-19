#!/usr/bin/env python3


lien_info = {
    'first_name': 'lien',
    'last_name': 'dinh',
    'age': '21',
    'height': '5\'4\"',
    'eye_color': 'brown',
    'hair_color': 'black',
    'favorite_foods': 'pizza',
    'favorite_language': 'c',
    'city': 'saigon',
    'country': 'vietnam',
    }

ngan_info = {
    'first_name': 'ngan',
    'last_name': 'dinh',
    'age': '23',
    'height': '5\'7\"',
    'eye_color': 'brown',
    'hair_color': 'black',
    'favorite_foods': 'thai foods',
    'favorite_language': 'haskell',
    'city': 'saigon',
    'country': 'vietnam',
    }

hong_info = {
    'first_name': 'hong',
    'last_name': 'tran',
    'age': '21',
    'height': '5\'5\"',
    'eye_color': 'brown',
    'hair_color': 'black',
    'favorite_foods': 'japanese foods',
    'favorite_language': 'java',
    'city': 'kuala lumpur',
    'country': 'Malaysia',
    }

people = [
    lien_info, ngan_info, hong_info
    ]

for person in people:
    full_name = person['first_name'] + " " + person['last_name']
    location = person['city'] + ", " + person['country']
    print("\n" + full_name.title() + "'s information"
          "\n\tAge: " + person['age'].title() +
          "\n\tHeight: " + person['height'].title() +
          "\n\tEye Color: " + person['eye_color'].title() +
          "\n\tHair Color: " + person['hair_color'].title() +
          "\n\tFavorite Foods: " + person['favorite_foods'].title() +
          "\n\tFavorite Lanagues: " + person['favorite_language'].title() +
          "\n\tLocation: " + location.title()
          )


