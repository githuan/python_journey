#!/usr/bin/env python3

# Define rivers
rivers = {
    'nile':'egypt',
    'amazon':'brazil',
    'ganges':'india',
    'mississippi':'mississippi',
    'danube':'ukraine',
    'yangtze':'shanghai',
    'mekong':'vietnam',
    'volga':'russia',
    'thames':'england',
    'zabezi':'zimbabwe',
    }

## Loops
# River descriptions
for key, value in rivers.items():
    if key == 'nile':
        print(key.title() + " river " +
              "is about 4,132 miles long. It runs through " +
              value.title() + "\n")
    if key == 'amazon':
        print(key.title() + " river " + "has about 4,100 miles long. " \
              "It's the widest river in the world; also run through " +
              value.title() + "\n")
    if key == 'ganges':
        print(key.title() + " river " + "is about 1,569 miles long. " \
              "It runs through " +
              value.title() + "\n")
    if key == 'mississipii':
        print(key.title() + " river " + "is about 2,340 miles long. " \
              "It runs through " +
              value.title() + "\n")
    if key == 'danube':
        print(key.title() + " river " + "is about 1,770 miles long. " \
              "It runs through " +
              value.title() + "\n")
    if key == 'yangtze':
        print(key.title() + " river " + "is 3,917 miles long also world's" \
              "third longest river. It runs through " +
              value.title() + "\n")
    if key == 'mekong':
        print(key.title() + " river " + "is 2,703 miles long; " \
              "world's 7th longest river. It runs throuh " +
              value.title() + "\n")
    if key == 'volga':
        print(key.title() + " river " + "is 2,294 miles long. " \
              "'Volga' means 'moisture' or 'wetness'. It runs through " +
              value.title() + "\n")
    if key == 'thames':
        print(key.title() + " river " + "is only 215 miles long. " \
              "It's once called 'dark water'; " \
              "was used to dispose of raw sewage. It runs through " +
              value.title() + "\n")
    if key == 'zabezi':
        print(key.title() + " river " + "is 1,599 miles long. " \
              "It runs through " +
              value.title() + "\n")

# List of rivers
print("\n\nHere is a list of 10 famous rivers:")
for river in sorted(rivers.keys()):
    print("\t" + river.title())

# List of countries rivers run throuh
print("\n\nHere is a list of states and countries that river runs through:")
for country in rivers.values():
    print("\t" + country.title())
