# Task: Write a program to check if a given number is positive, negative or 0.

# Hint: First input a number and by using if, elif and else statements check the number.

# Solution:
number = int(input("Input a number: "))

if number > 0:
    print("Number is positive!")
elif number < 0:
    print("Number is negative!")
else:
    print("Number is zero!")
