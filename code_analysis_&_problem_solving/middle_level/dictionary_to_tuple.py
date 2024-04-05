# Task: Write a python program that converts the dictionary to tuple pairs.

# Hint: We use the function "items" to display the dictionary to tuple pairs.

# Solution:
def dict_to_tuple():
    x = {1: "one", 2: "two", 3: "three"}

    for i in x.items():
        print(i)


dict_to_tuple()