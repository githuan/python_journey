#!/usr/bin/env python3


print("\nBeautiful Cities:")

def describe_city(city_name, city_location):
    """Display city information."""
    print(f"\t{city_name.title()} is in {city_location.title()}.")


describe_city('reykjavik', 'iceland')
describe_city('saigon', 'vietnam')
describe_city('kiev', 'ukraine')
describe_city('moscow', 'russia')
describe_city('new york', 'u.s.a')
