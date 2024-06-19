# Task: Create an iterable & iterator object with the next functionality:
# It will be created an instance of class Text, that has an atribute 'text'.
# This can be a text/paragraph/phrase.
# The object will be iterable and iterator.
# The phrase will be splited such that it can iterate through each word in text.

# Hint: iterable -> it's an object through which we can iterate (loop over).
# __iter__ -> when we iterate through the elements of a list or tuple, this method is called.
# iterated object -> it's an object which has __next__ method implemented behind.
# map function -> receives as an argument other function and an iterable object.


# Solution:

class Text:
    def __init__(self, text):
        self.text = text
        self.cuvinte = self.text.split(' ')
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cuvinte):
            raise StopIteration
        ind = self.index
        self.index += 1
        return self.cuvinte[ind]


txt = Text('We learn python every day!')

for item in txt:
    print(item)

