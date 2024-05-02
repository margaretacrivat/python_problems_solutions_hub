# Task:  Write a program that displays the number of digits of a given number from the keyboard.

# Solution:
no = int(input("Input a number: "))   #for example: 3250
counter = 0

while no != 0:
    counter = counter + 1
    no = no // 10

print(counter)
