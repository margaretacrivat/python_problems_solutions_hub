# Task: Which pizza has the best price/quantity ratio?
# Write a program (or function) that will compare the area/price ratio between two pizzas.
# In order to calculate the area of a circle P at a given radius r - use this formula:
# A =  pi (3.14159) x r2
# Find a restaurant in your area, enter the appropriate data and answer the question asked in the recommendation.

# Hint: It's worth creating a function that computes the whole so that it doesn't repeat itself twice.


# Solution 1

radius1 = 32
radius2 = 36
price1 = 15
price2 = 20


def circle_area_to_price(radius, price):

    pi = 3.14
    area = pi * radius * radius
    return area/price


print(circle_area_to_price(radius1, price1))
print(circle_area_to_price(radius2, price2))


# Solution 2

# Here's a Python program that compares the area/price ratio between two pizzas. '
# You'll need to input the radius and price for each pizza, and the program will calculate and compare the
# area/price ratio for both pizzas.


# import math

# def calculate_area(radius):
#     return math.pi * (radius ** 2)

# def main():
#     print("Pizza 1:")
#     radius1 = float(input("Enter the radius of the first pizza (in inches): "))
#     price1 = float(input("Enter the price of the first pizza (in dollars): "))
#
#     print("\nPizza 2:")
#     radius2 = float(input("Enter the radius of the second pizza (in inches): "))
#     price2 = float(input("Enter the price of the second pizza (in dollars): "))

#     area1 = calculate_area(radius1)
#     area2 = calculate_area(radius2)

#     ratio1 = area1 / price1
#     ratio2 = area2 / price2

#     if ratio1 > ratio2:
#         print("Pizza 1 has a better area/price ratio.")
#     elif ratio2 > ratio1:
#         print("Pizza 2 has a better area/price ratio.")
#     else:
#         print("Both pizzas have the same area/price ratio.")

