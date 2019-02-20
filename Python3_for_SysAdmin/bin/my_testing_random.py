#!/usr/bin/env python3.7

# Looping through a random number.

import random

count = 0
x = int(random.uniform(1.0, 100))

print(f"We've got a random number: {x}")

while count <= x:
    if count % 2 ==0:
        count += 1
        continue
    print(f"The following are its odd numbers: {count}")
    count += 1
