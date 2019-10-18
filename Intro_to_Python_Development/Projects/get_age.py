#!/usr/bin/env python3

# Import library
from datetime import datetime

# Get current year
current_year = datetime.now().year

# Ask user's input
year_born = input('What year did you born? ')

# Calculate ages
age = current_year - int(year_born)
print(f'You are now {age} of ages.')