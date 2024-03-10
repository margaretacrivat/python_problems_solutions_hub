# Please create a pseudocode function that will check if all the words in an array are palindromes.
# For example, an input of ['racecar', 'noon', 'civic'] should return True, but an input of ['racecar', 'shoe', 'moon']
# should return False.


# Solution
# PSEUCODOCE:

# function reverse_word(string word)
# reversed = ""
# for letter in word:
#     reversed = letter + reversed
# return reversed
#
# function
# is_palindrome(string
# word)
# return word == reverse_word(word)
#
# function
# check_all_palindromes(array
# arr)
# for word in arr:
#     if is_palindrome(word) == false
#         return false
# return true


# PSEUDOCODE CONVERTED TO PYTHON CODE:
def reverse_word(word):
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word


def is_palindrome(word):
    return word == reverse_word(word)


def check_all_palindromes(arr):
    for word in arr:
        if not is_palindrome(word):
            return False
    return True


# Test the function
arr1 = ['racecar', 'noon', 'civic']
arr2 = ['racecar', 'shoe', 'moon']

print(check_all_palindromes(arr1))  # Should return True
print(check_all_palindromes(arr2))  # Should return False


# This solution is more closely to good programming practices and principles.
# Here's why:
# Modularity: separates the logic for reversing a word into its own function (reverse_word) and the logic for checking
# if a word is a palindrome into another function (is_palindrome). This modular approach makes the code more readable,
# maintainable, and reusable.

# Use of Functions: Breaking down the problem into smaller, reusable functions makes the code more organized and easier
# to understand. It promotes code reuse and makes testing and debugging simpler.

# Looping Through the Array: Instead of hard coding checks for individual elements of the array, loops through the
# array, checking each word individually.
# This makes the code more scalable and adaptable to arrays of different lengths without having to modify the code
# structure.

# Boolean Return: directly returns the result of the palindrome check using a boolean value (true or false).
# This is a more direct and clear way of expressing the outcome of the function.
