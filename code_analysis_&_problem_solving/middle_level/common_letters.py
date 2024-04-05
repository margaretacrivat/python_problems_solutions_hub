# Task: Find out the common letters between two strings.

# Hint: first delete all duplicates, to remain with unique letters.

# Solution:
def common_letters():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    # all duplicates are removed
    s1 = set(str1)
    s2 = set(str2)

    # operation for extracting common letters
    list_letters = s1 & s2
    print(list_letters)


common_letters()



