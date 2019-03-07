#!/usr/bin/env python3


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
fiance_foods = my_foods[-3:]

print("My favorite foods are:")
#print(my_foods)
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
#print(friend_foods)
for food in friend_foods:
    print(food.title())

print("\nMy fiance's favorite foods are:")
#print(fiance_foods)
for food in fiance_foods:
    print(food.title())

