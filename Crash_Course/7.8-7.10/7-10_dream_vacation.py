#!/usr/bin/env python3


responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("What is your name? ")
    response = input("If you could visit one place in the world, " + 
                     "where would you go? ")
    
    # Store the response in the dictionary.
    responses[name] = response
     
    # Find out if anyone else want take the poll.
    repeat = input("Would you like another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")
