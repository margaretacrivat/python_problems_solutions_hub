# Please create a function that can check if a given number n is prime or not,
# where n > 1.

# Solution
# PSEUDOCODE

# function isPrime(number n)
#     for i from 2 to square root of n rounded down inclusive
#         if n mod i is 0
#             return false
#
#     return true

# Pseudocode is a plain language description of the steps or logic of a computer program, designed to be easily
# understood by humans. It is often used during the initial stages of program design or algorithm development before
# translating the logic into a specific programming language like Python, Java, C++, etc.

# Python implementations of the function based on the provided pseudocode:

import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(11))  # Output: True
print(is_prime(15))  # Output: False


# This function is the most efficient in terms of both memory efficiency and time complexity.
# Here's why:

# Memory Efficiency:
# It only uses a single variable i for iteration. It does not require storing any additional data structures
# like arrays, which saves memory.

# Time Complexity:
# It has a time complexity of O(sqrt(n)), where n is the input number. It only needs to check divisibility up to the
# square root of the input number, which reduces the number of iterations significantly compared to iterating up to
# n or n-1.



