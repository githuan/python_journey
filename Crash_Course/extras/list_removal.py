#!/usr/bin/env python3

motorcycles = ['honda', 'yamaha', 'kawasaki', 'suzuki']
print(motorcycles)

not_favorite = 'yamaha'
motorcycles.remove(not_favorite)
print(motorcycles)
print("\nI remove " + not_favorite.title() + " brand because is not my favorite.")
