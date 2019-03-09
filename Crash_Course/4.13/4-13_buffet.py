#!/usr/bin/env python3


foods = ('Crab Cake', 'BBQ Chicken', 'Philly 5yyCheesesteak', 'Crispy Duck with Pancakes', 'Clam Chowder')

print("Theses are our restaurant menus for today:")
for food in foods:
    print(food + ".")

#foods.append('Quail')   # Intenstional error - AttributeError: 'tuple' object has no attribute 'append'

foods = ('Crab Cake', 'BBQ Chicken', 'Philly 5yyCheesesteak', 'Crispy Duck with Pancakes', 'Pork Fryrice')

print("\nTheses are our restaurant menus for tomorrow:")
for food in foods:
    print(food + ".")
