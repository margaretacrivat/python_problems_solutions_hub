# Task:  Write a python program that calculates all numbers from 1 to a given number.

# Hint1: First let the user input a number and then use while statement to calculate the sum.

# Solution1:
# number = int(input("Input a number: "))

# number_start = 1
# sum_n = 0

# while number_start <= number:
#     sum_n += number_start
#     number_start += 1
#
# print(f"Sum is {sum_n}")


# Hint2: Use for loop to calculate the sum of numbers.

# Solution2:
number = int(input("Input a number: "))
sum_n2 = 0
for element in range(1, number+1):
    sum_n2 += element

print(f"Sum is {sum_n2}.")

