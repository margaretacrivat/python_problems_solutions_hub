# Task: Write a program that sorts dictionary by values.
# If they are strings, sort them by the key length.

# Hint: use dictionary comprehension to create your dictionary.

# Solution:
programming_class = {"java": 14, "python": 12, "javascript": 8, "C": 9}

# dictionary sorted by values
sorted_items = sorted(programming_class.items(), key=lambda item:item[1])
print(sorted_items)

# create my own dictionary
sorted_items_keys = {k:v for k,v in sorted_items}
print(sorted_items_keys)

# sort by key length
sorted_items_keys = sorted(programming_class.items(), key=lambda item:len(item[0]))
print(sorted_items_keys)



