#!/user/bin/env python3

pizzas = ['neapolitan', 'chicago', 'new york style', 'sicillian', 'greek']
pizzas.sort(reverse=True)

for pizza in pizzas:
    print("I like " + pizza.title() + " pizza.\n")

print("I love pizzas!")
