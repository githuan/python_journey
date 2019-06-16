#!/usr/bin/env python3


def city_country(city, country):
    """Return a full city, country neatly formatted."""
    full_city_country = f"{city}, {country}"
    return full_city_country.title()


new_york = city_country('new york', 'u.s.a.')
print(new_york)
kiev = city_country('kiev', 'ukraine')
print(kiev)
moscow = city_country('moscow', 'russia')
print(moscow)
