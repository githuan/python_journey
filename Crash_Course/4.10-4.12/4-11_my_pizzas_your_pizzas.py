#!/user/bin/env python3

# Define list
my_pizzas = ['neapolitan', 'chicago', 'new york style', 'sicillian', 'greek']
friend_pizzas = my_pizzas[:]
fiance_pizzas = my_pizzas[:]

# Modify list
my_pizzas.append('philly cheesesteak')

friend_pizzas.append('margherita')

fiance_pizzas.pop()
fiance_pizzas.pop()
fiance_pizzas.append('philly cheesesteak')
fiance_pizzas.append('bbq chicken')
fiance_pizzas.append('seafood')
fiance_pizzas.append('fruit')

# Organize list
my_pizzas.sort()
friend_pizzas.sort()
fiance_pizzas.sort(reverse=True)

# Loop and print result
print("My favorite pizzas are:")
for name in my_pizzas:
    print(name.title())

print("\nMy friends' favorite pizzas are:")
for name in friend_pizzas:
    print(name.title())

print("\nMy favorite pizzas are:")
for name in fiance_pizzas:
    print(name.title())
