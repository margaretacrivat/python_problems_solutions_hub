# Task: Give an example on a built-in function which creates an iterable object, that in the same time is an iterator.
# Use the function in an example.
# Which is the difference between iterator and an iterable object?
# Give examples of iterable data types.

# Hint: iterable -> it's an object through which we can iterate (loop over).
# __iter__ -> when we iterate through the elements of a list or tuple, this method is called.
# iterated object -> it's an object which has __next__ method implemented behind.
# map function -> receives as an argument other function and an iterable object.


# Solution:

l_list = [1, 2, 3]

for item in l_list:
    print(item)

# ----------------------

eur_prices = [1, 5, 500]


def convert_to_ron(eur):
    return f'{eur * 5} RON'


f = map(convert_to_ron, eur_prices)

for item in f:
    print(item)



