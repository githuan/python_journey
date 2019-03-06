#!/usr/bin/env python3

deserts = ['cheese cake', 'apple pie', 'chocolate chips cookie', 'mango jelly', 'icecream']

#print(deserts[5])       # Intentional Error #1
print(deserts[4] + "\t\t <-- Uses list index in range.")       # Correction - Index starts at 0 not 1; Therefore, 0-4 are the valid indexes #
print(deserts[-1] + "\t\t <-- Uses list index in range with '-'.")      # Same above but using "-" to access the last index

del deserts[2]
deserts.pop(-2)
deserts.remove('apple pie')
deserts.pop()
deserts.pop()

#print(deserts[0])       # Intentional Error #2
print(str(deserts) + "\t\t\t <-- Prints an empty list because there is no more index within a list.")          # Correction - The list is empty, nothing to print. Print empty list instead
