# Task: Prime numbers (what if they are second?)
# Write a program that checks if a given number is preceded by a prime number.
# (prime number is a whole number greater than 1 whose only factors are 1 and itself.
# A factor is a whole number that can be divided evenly into another number.)

# When checking if n is prime, you don't need to check potential divisors from 2 to n.
# You can dramatically reduce the number of comparisons by only checking from 2 to √ (n) (root of n).

# Example:
# Let's try to find all the divisors of 100 and list them in the form of a table:

# 2  x  50 = 100
# 4  x  25 = 100
# 5  x  20 = 100
# 10  x  10 = 100 <-- √(100)
# 20  x  5  = 100
# 25  x  4  = 100
# 50  x  2  = 100

# It can be seen that by reaching √ (100) - all divisors have already been found.
# This property applies to any value of n.

# It's best to start by checking if the number you are checking is two, one, or divisible by 2.


import math


def previous_is_prime(second):
    first = second - 1

    if first == 2:
        return True
    if first % 2 == 0 or first <= 1:
        return False

    sqr = int(math.sqrt(first)) + 1

    for divisor in range(3, sqr, 2):
        if first % divisor == 0:
            return False
    return True


print(previous_is_prime(9))