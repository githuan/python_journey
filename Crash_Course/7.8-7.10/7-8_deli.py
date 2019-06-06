#!/usr/bin/env python3


# Start with a list of sandwich orders that need to be made,
# and an empty list to hold made sandwich orders.
sandwich_orders = ['cheesesteak', 'Po-boy', 'breakfast', 'reuben', 'the parms',
                   'roast beef', 'banh mi', 'grilled cheese', 'pulled pork',
                   'ham', 'lobster roll', 'the cuban', 'italian hero',
                   'portchetta', 'chicken biscuit', 'B.L.T.', 'croque madame']
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
    print(finished_sandwich.title())
