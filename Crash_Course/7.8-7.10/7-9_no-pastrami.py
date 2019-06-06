#!/usr/bin/env python3


# Start with a list of sandwich orders that need to be made,
# and an empty list to hold made sandwich orders.
sandwich_orders = ['cheesesteak', 'pastrami', 'Po-boy', 'breakfast', 'reuben',
                   'the parms', 'pastrami', 'roast beef', 'banh mi',
                   'grilled cheese', 'pastrami', 'pulled pork', 'ham',
                   'lobster roll', 'pastrami', 'the cuban', 'italian hero',
                   'portchetta', 'pastrami', 'chicken biscuit', 'B.L.T.',
                   'croque madame']

print("\n\n*Deli has run out of pastrami*\n\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

# Verify each sandwich order until there are no more sandwich to be made.
# Move each verified sandwich order into the list of finished sandwich orders.
while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"I made your {current_order.title()} sandwich.")
    finished_sandwiches.append(current_order)

# Display all finished sandwich orders.
print("\nThe following sandwich have been made:")
for finished_sandwich in finished_sandwiches:
    print(f"\t{finished_sandwich.title()}")
