#!/usr/bin/env python3


# Define favorite languages
favorite_languages = {
    'fred': ['c', 'c#'],
    'janna': ['java', 'javascript', 'node.js'],
    'link': ['lua', 'python'],
    'mark': ['c#', 'python', 'c', 'c++', 'haskell'],
    'john': ['assembly', 'haskell', 'c'],
    'thuan': ['python', 'go'],
    'selena': ['java', 'javascript'],
    'thuan': ['c', 'c++'],
    'komos': ['ruby', 'python', 'php'],
    'vicktor': ['c++', 'php'],
    }

# Define friends list
friends = [
    'janna', 'mark', 'komos', 'scott', 'amelie', 'ashley', 'rachel',
    'benjamin', 'thuan', 'selena', 'vicktor'
    ]

for name, languages in favorite_languages.items():
    if name in friends:
        print("\nHi " + name.title() + ", your favorite languages are:")
        for language in sorted(languages):
            if language == 'javascript':
                print("\tJavaScript")
            elif language == 'node.js':
                print("\tNode.JS")
            elif language == 'php':
                print("\tPHP")
            else:
                print("\t" + language.title())
    
for friend in friends:
    if friend not in favorite_languages.keys():
        print(friend.title() + ", please take our poll.\n")
