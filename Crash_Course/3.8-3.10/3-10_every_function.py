#!/usr/bin/env python3

# Orignal List
languages = ['mandarin chinese', 'english', 'hindustani', 'spanish', 'arabic', 'malay', 'russian', 'bengali', 'portuguese', 'french']

print("The original list of top 10 spoken languages:")
print("\n1. " + languages[0].title() + \
      "\n2. " + languages[1].title() + \
      "\n3. " + languages[2].title() + \
      "\n4. " + languages[3].title() + \
      "\n5. " + languages[4].title() + \
      "\n6. " + languages[5].title() + \
      "\n7. " + languages[6].title() + \
      "\n8. " + languages[7].title() + \
      "\n9. " + languages[8].title() + \
      "\n10. " + languages[9].title())

# Replace French with Vietnamese
print("\nReplace French using 'index':")
languages[9] = 'vietnamese'

print("The new list of top 10 spoken languages:")
print("\n1. " + languages[0].title() + \
      "\n2. " + languages[1].title() + \
      "\n3. " + languages[2].title() + \
      "\n4. " + languages[3].title() + \
      "\n5. " + languages[4].title() + \
      "\n6. " + languages[5].title() + \
      "\n7. " + languages[6].title() + \
      "\n8. " + languages[7].title() + \
      "\n9. " + languages[8].title() + \
      "\n10. " + languages[9].title())

# Append French to the list
print("\nAdd French to the end of the list using 'append()' function:")
languages.append('french')

print("The new list of top 11 spoken languages:")
print("\n1. " + languages[0].title() + \
      "\n2. " + languages[1].title() + \
      "\n3. " + languages[2].title() + \
      "\n4. " + languages[3].title() + \
      "\n5. " + languages[4].title() + \
      "\n6. " + languages[5].title() + \
      "\n7. " + languages[6].title() + \
      "\n8. " + languages[7].title() + \
      "\n9. " + languages[8].title() + \
      "\n10. " + languages[9].title() + \
      "\n11. " + languages[10].title())

# Insert Japanese before Vietnamese
print("\nInsert Japanese before Vietnamese to the list using 'insert()' function:")
languages.insert(9, 'japanese')

print("The new list of top 12 spoken languages:")
print("\n1. " + languages[0].title() + \
      "\n2. " + languages[1].title() + \
      "\n3. " + languages[2].title() + \
      "\n4. " + languages[3].title() + \
      "\n5. " + languages[4].title() + \
      "\n6. " + languages[5].title() + \
      "\n7. " + languages[6].title() + \
      "\n8. " + languages[7].title() + \
      "\n9. " + languages[8].title() + \
      "\n10. " + languages[9].title() + \
      "\n11. " + languages[10].title() + \
      "\n12. " + languages[11].title())

# Remove Vietnamese
print("\nRemove Vietnamese using del command:")
del languages[10]

print("The new list of top 11 spoken languages:")
print("\n1. " + languages[0].title() + \
      "\n2. " + languages[1].title() + \
      "\n3. " + languages[2].title() + \
      "\n4. " + languages[3].title() + \
      "\n5. " + languages[4].title() + \
      "\n6. " + languages[5].title() + \
      "\n7. " + languages[6].title() + \
      "\n8. " + languages[7].title() + \
      "\n9. " + languages[8].title() + \
      "\n10. " + languages[9].title() + \
      "\n11. " + languages[10].title())

# Remove French
print("\nRemove last language using 'pop()' function:")
languages.pop()

print("The new list of top 10 spoken languages:")
print("\n1. " + languages[0].title() + \
      "\n2. " + languages[1].title() + \
      "\n3. " + languages[2].title() + \
      "\n4. " + languages[3].title() + \
      "\n5. " + languages[4].title() + \
      "\n6. " + languages[5].title() + \
      "\n7. " + languages[6].title() + \
      "\n8. " + languages[7].title() + \
      "\n9. " + languages[8].title() + \
      "\n10. " + languages[9].title())

# Remove Bengali
print("\nRemove a specific language from the list using 'pop()' function and its position:")
languages.pop(-3)

print("The new list of top 9 spoken languages:")
print("\n1. " + languages[0].title() + \
      "\n2. " + languages[1].title() + \
      "\n3. " + languages[2].title() + \
      "\n4. " + languages[3].title() + \
      "\n5. " + languages[4].title() + \
      "\n6. " + languages[5].title() + \
      "\n7. " + languages[6].title() + \
      "\n8. " + languages[7].title() + \
      "\n9. " + languages[8].title())

# Remove Malay
print("\nRemove a specific language using 'remove()' function: (This method will only remove the first occurence)")
languages.remove('malay')

print("The new list of top 8 spoken languages:")
print("\n1. " + languages[0].title() + \
      "\n2. " + languages[1].title() + \
      "\n3. " + languages[2].title() + \
      "\n4. " + languages[3].title() + \
      "\n5. " + languages[4].title() + \
      "\n6. " + languages[5].title() + \
      "\n7. " + languages[6].title() + \
      "\n8. " + languages[7].title())

# Remove Hindustani
print("\nRemove a specific language using variable and 'remove()' function: (This method only remove the first occurence)")
remove_lang = 'hindustani'
languages.remove(remove_lang)

print("The new list of top 7 spoken languages:")
print("\n1. " + languages[0].title() + \
      "\n2. " + languages[1].title() + \
      "\n3. " + languages[2].title() + \
      "\n4. " + languages[3].title() + \
      "\n5. " + languages[4].title() + \
      "\n6. " + languages[5].title() + \
      "\n7. " + languages[6].title())

# Temp sort
print("\nTemporary sort list using 'sorted()' function:")
print(sorted(languages))

# Temp sort reverse
print("\nTemporary sort reverse list using 'sorted(list_name, reverse=True' function:")
print(sorted(languages, reverse=True))

# Reverse order
print("\nReverse list using 'reverse()' function:")
languages.reverse()
print(languages)

# Reverse order again
print("\nReverse again:")
languages.reverse()
print(languages)

# Perm sort
print("\nPermanently sort order of a list using 'sort()' function:")
languages.sort()
print(languages)

# Perm sort reverse
print("\nPermanently sort reverse order of a list using 'sort(reverse=True)' function:")
languages.sort(reverse=True)
print(languages)

# Count languages
print("\nThere are exactly " + str(len(languages)) + " languages remain in the list right now.")
