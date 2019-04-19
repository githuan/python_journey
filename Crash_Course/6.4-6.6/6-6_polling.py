#!/usr/bin/env python3

# Define favorite languages
fav_lang = {
    'fred':'c',
    'janna':'java',
    'link':'lua',
    'mark':'c#',
    'john':'assembly',
    'thuan':'python',
    'selena':'java',
    'thuan':'c',
    'komos':'ruby',
    'vicktor':'c++',
    }

# Define friends list
friends = [
    'janna', 'mark', 'komos', 'scott', 'amelie', 'ashley', 'rachel',
    'benjamin', 'thuan', 'selena', 'vicktor'
    ]

for name,lang in fav_lang.items():
    if name in friends:
        print("Hi " + name.title() +
              ", I see your favorite language is " +
              lang.title() + "!\n"
              )
    
for friend in friends:
    if friend not in fav_lang.keys():
        print(friend.title() + ", please take our poll.\n")
