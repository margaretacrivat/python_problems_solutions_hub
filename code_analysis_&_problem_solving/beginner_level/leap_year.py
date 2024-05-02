# Task: Write a program that verifies if the year is leap year.

# Hint: for the year to be leap year it has to:
# - to be divisible by 4.
# - to not be divisible by 100, but if it is, to be divisible by 400.

# Solution 1:
year = int(input("Input a year:"))

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
        if year % 400 == 0:
            leap = True
    return leap

print(is_leap(year))


# Solution 2:
# year = int(input("Input a year:"))
#
# def is_leap(year):
#     if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
#         return True
#     else:
#         return False
# print(is_leap(year))

