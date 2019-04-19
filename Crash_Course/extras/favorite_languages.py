#!/usr/bin/env python3


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
    if len(languages) <= 1:
        print("\n" + name.title() + "'s favorite languages is:")
    for language in languages:
        print("\t" + language.title())
