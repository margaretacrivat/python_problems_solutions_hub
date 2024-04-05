# Task: Write a python program to count the frequency of words appearing in a string.

# Hint: First split the words and put them into a list.

# Solution 1:
# def words_frequency():
#     str_phrase = input("Enter a string: ")
#     li_words = str_phrase.split()    # it splits the words and put them into a list
#     d = {}
#
#     for i in li_words:
#         if i not in d.keys():
#             d[i] = 0          # it will initialize the dictionary as 0
#         d[i] = d[i] + 1       # it will initialize by 1 as the word appears
#     print(d)
#
#
# words_frequency()


# Solution 2:
# change in the for:

def words_frequency():
    str_phrase = input("Enter a string: ")
    li_words = str_phrase.split()
    d = {}

    for i in li_words:
        d[i] = d.get(i, 0) + 1  # initialize it to 0 and increment it by 1 in the same step
    print(d)


words_frequency()






