# Task: Create two sets named "set1" and "set2" and add different elements to each of them.
# Using the difference() method, find out which elements are different in the two sets.

# Hint: First find out which elements in set 1 are different from set 2 and then reverse.

# Solution:
set1 = {"apples", "pears", "kiwi"}
set2 = {"mango", "pears", "kiwi"}

set3 = set1.difference(set2)
print(set3)

set4 = set2.difference(set1)
print(set4)
