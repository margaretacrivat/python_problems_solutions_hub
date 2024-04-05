# Task: Write a python program that converts two lists into a dictionary.

# Hint: We use "zip" to map keys with the values and "dict" to make it to dictionary.

# Solution:
def list_to_dict():
    keys = [1, 2, 3]
    values = ["one", "two", "three"]
    result = dict(zip(keys, values))
    print(result)


list_to_dict()