# Task: Write a program that checks the length of the given string.

# Hint: First let the user input the string and by using if, elif and else statements check the string length.

# Solution:
string = input("Enter a string: ")
if len(string) < 5:
    print("String is short!")
elif len(string) >= 5 and len(string) < 10:
    print("String is medium!")
else:
    print("String is long!")
