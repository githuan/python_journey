#!/usr/bin/env python3


cities = {
    'kiev': {
        'fact' : 'Kiev known to Russian as the "Mother of Russian cities."',
        'population': '3.14 million',
        'country': 'ukriane',
    },
    'moscow': {
        'fact' : 'Moscow is home of a record numbers of dollar millionires.',
        'population': '11.92 million',
        'country': 'russia',
    },
    'prague': {
        'fact' : 'You can actually have beer spa in Prague.',
        'population': '1.281 million',
        'country': 'czech republic',
    },
    'dallas': {
        'fact' : 'The first ever professional cheerleading squad came from Dallas.',
        'population': '1.341 million',
        'country': 'united states of america',
    },
    'new york': {
        'fact' : 'The Empire State building gets hit by lightning about 23 times per year.',
        'population': '8.623 million',
        'country': 'united states of america',
    },
}

for city_name, city_info in cities.items():
    print("\nCity: " + city_name.title())
    print("\tOne fact about " + city_name.title() + ": " + city_info['fact'])
    print("\tA population of " + city_info['population'] + " people.")
    print("\tLocate in " + city_info['country'].title() + ".")
