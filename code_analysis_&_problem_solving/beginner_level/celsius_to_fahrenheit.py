# Task: Write a python program that asks the user to input a temperature in Celsius degree and then display the
# equivalent temperature in Fahrenheit degree.

# Hint: Conversion formula is -> F = C * 1.8 + 32

# Solution:
c = input("Celsius degree: ")
c = int(c)
f = c * 1.8 + 32
print(f'Fahrenheit degree is: {f}F')
