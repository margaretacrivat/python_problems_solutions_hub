# Task:  Write a program to display numbers from a list using for loop by taking into account the following:
# - if the number is divisible by 5, display it;
# - if the number is > 150, pass to the next number;
# - if the number is > 500 get out of the loop.

# Solution:
list_numbers = [12, 75, 150, 180, 145, 525, 50]

for number in list_numbers:
    if number % 5 == 0 and number < 150:
        print(number)
    elif number > 150 and number < 500:
        continue
    elif number > 500:
        break

