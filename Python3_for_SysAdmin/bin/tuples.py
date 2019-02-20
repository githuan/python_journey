#!/usr/bin/env python3.7

# Tuples

print("# Tuples are fix width, immutable sequence type.\nWe create typles using parenthesis () and at least one comma ,:\npoint = (1, 2, 3, 4, 5)\n\n")

print("# Tuples are immutable, we do not have\naccess to the same methods that we do on a list.\nWe can use typles in some operations\nlike concatenation, but we cannot change the original\ntuple that we created.\nmap_point = point + ('a', 'b', 'c',)\nmap_point\n(1, 2, 3, 4, 5, 'a', 'b', 'c')\n\n")

print("# One interesting characteristic of typles is\nthat we can unpack them into multiple variables at the same time:\none, two, three, four, five, x, y, z = map_point\nfour\n4\nx\n'a'\ny\n'b'\nz\n'c'\n\n")

print("# The time you are most likely to see typles\nwill be when looking at a format string\nthat has compatible with Python 2:\nprint(\"The most frequently used phrase is: %s %s %s\" % (\"I\",\"love\",\"you\"))\nThe most frequently used phrase is: I love you\n\n")

print("# For a single word subtitution, parenthesis is not required:\nprint(\"The most powerful word is: %s\" % \"Love\"\nThe most powerful word is: Love")
