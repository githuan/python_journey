#!/user/bin/env python3

# Variable
fruits = []

# Modify variable
fruits.append('orange')
fruits.append('mango')
fruits.append('kiwi')
fruits.append('dragon fruit')
fruits.append('jack fruit')
fruits.append('apple')
fruits.append('banana')
fruits.append('pineapple')
fruits.append('pear')
fruits.append('coconut')
fruits.append('watermelon')

fruits.sort() # Sort

dislike_fruits = []

for fruit in fruits:
    if fruit == 'orange':
        print("\n" + fruit.title() + "! You're on track of Vitamin C.")
    if fruit == 'mango':
        print("\n" + fruit.title() + "! I like " + fruit.title() + "s too! " +
              "Make sure you eat them ripe.")
    if fruit == 'apple':
        print("\n" + fruit.title() + "! An apple a day keep you away from " +
              "the doctor.")
    if fruit == 'banana':
        print("\n" + fruit.title() + "! You really like " + fruit.title() +
              ".")
    if fruit == 'pineapple':
        print("\n" + fruit.title() + "! Yummy " + fruit.title() + ".")
    if fruit == 'coconut':
        print("\n" + fruit.title() + "! It's delicious with cocktails.")
    if fruit == 'watermelon':
        print("\n" + fruit.title() + "! Costco has them on sale during the " +
              "season.")
    if fruit != 'orange' and fruit != 'mango' and fruit != 'apple' \
       and fruit != 'banana' and fruit != 'pineapple' and fruit != 'coconut' \
       and fruit != 'watermelon':
        dislike_fruits.append(fruit)

print("\nThese are not my favorite fruits: ")

for fruit in dislike_fruits:
    print(fruit.title())
