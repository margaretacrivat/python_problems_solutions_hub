# Task: Dancing parabolas
# Write a function (or program) that will calculate the zeros of the given square function.
# For this purpose, you can use the formulas presented here:
# The zeros of a function are the values of x when f(x) is equal to 0. f(x) = 0, x is a zero of the function

# We assume movement only in the space of real numbers, complex solutions are not required.
# In order to accomplish the task, it is best to create a function that will accept 3 arguments being the
# coefficients of the equation of the quadratic function.
# The math library for the square root calculation will also be useful.

import math


def find_roots(a, b, c):

    if a == 0:
        print("Input incorrect quadratic equation")
        return

    delta = b * b - 4 * a * c
    sqrt_delta = math.sqrt(abs(delta))

    if delta > 0:
        print("two solutions")
        print(f'x_1 = {(-b + sqrt_delta) / (2 * a)}')
        print(f'x_2 = {(-b - sqrt_delta) / (2 * a)}')

    elif delta == 0:
        print("one solution")
        print(-b / (2 * a))

    elif delta < 0:
        print("no solution")


find_roots(2,4,1)
