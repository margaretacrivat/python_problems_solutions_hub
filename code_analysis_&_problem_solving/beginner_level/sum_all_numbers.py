# Task:  Write a python program that calculates the sum of all numbers from 1 to a given number.

# Hint1: Let the user input a number and then by using while loop calculate the sum of the numbers.

# Solution1:
# number = int(input("Enter a number: "))
#
# num = 1
# sum_n1 = 0
#
# while num <= number:
#     sum_n1 += num
#     num += 1
#
# print(f"Sum is {sum_n1}.")


# Hint2: Let the user input a number and then by using for loop calculate the sum of the numbers.

# Solution1:
number = int(input("Enter a number: "))
sum_n2 = 0
for element in range(1, number+1):
    sum_n2 += element

print(f"Sum of the numbers is {sum_n2}.")

