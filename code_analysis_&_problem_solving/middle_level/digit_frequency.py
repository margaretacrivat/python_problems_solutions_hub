# Given an input integer n, create a while loop that utilizes arithmetic to store the frequency of each digit present
# in n in a dictionary frequency_map. The input number n will be provided as a numeric data type, not a string.
# For each loop iteration, you must update frequency_map before reducing n.


# Solution
# Pseudocode steps:

# initialize an empty dictionary frequency_map
# while n is greater than 0
# digit = n mod 10
# if digit is not in frequency_map keys
# add digit to frequency_map with an initial value of 1
# else add 1 to the value of digit in frequency_map
# n = integer part of (n / 10)


# This arrangement ensures that the frequency of each digit in the input number n is correctly stored in the
# frequency_map dictionary.


def digit_frequency(n):
    # initialize an empty dictionary frequency_map
    frequency_map = {}
    while n > 0:
        digit = n % 10
        if digit not in frequency_map:
            frequency_map[digit] = 1  # if digit is not in frequency_map keys, add it with an initial value of 1
        else:
            frequency_map[digit] += 1  # else add 1 to the value of digit in frequency_map
        n = n // 10  # n = integer part of (n / 10)
    return frequency_map


# Test the function
input_number = 1234567890
result = digit_frequency(input_number)
print(result)


# This code defines a function digit_frequency that takes an input integer n and returns a dictionary frequency_map
# containing the frequency of each digit in n. It iterates through each digit of n using a while loop, updating the
# frequency_map accordingly. Finally, it tests the function with an example input.

