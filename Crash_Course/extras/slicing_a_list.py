#!/usr/bin/env python3

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3]) # ['charles', 'martina', 'michael']
print(players[1:4]) # ['martina', 'michael', 'florence']
print(players[:4])  # ['charles', 'martina', 'michael', 'florence']
print(players[2:])  # ['michael', 'florence', 'eli']
print(players[-3:]) # ['michael', 'florence', 'eli']

print("\nHere are the players on my teams:")
for player in players[:3]:
    print(player.title())

print("\nHere are the players on my team:")
for player in players[1:4]:
    print(player.title())

print("\nHere are the players on my team:")
for player in players[:4]:
    print(player.title())

print("\nHere are the players on my team:")
for player in players[2:]:
    print(player.title())

print("\nHere are the players on my teams:")
for player in players[-3:]:
    print(player.title())

