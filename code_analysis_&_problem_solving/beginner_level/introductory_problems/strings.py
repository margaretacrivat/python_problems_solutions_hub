# STRINGS

# Task 1: Use the len method to print the length of the string.

# Solution
x = "Hello World"
print(len(x))


# Task 2: Get the first character of the string txt.
# Solution
txt = "Hello World"
x = txt[0]


# Task 3: Get the characters from index 2 to index 4 (llo).

# Solution
txt = "Hello World"
y = txt[2:5]
print(y)

# Task 4: Return the string without any whitespace at the beginning or the end.

# Solution
txt = " Hello World "
z = txt.strip()
print(z)


# Task 4: Convert the value of txt to upper case.

# Solution
txt = "Hello World"
txt1 = txt.upper()
print(txt1)


# Task 5: Convert the value of txt to lower case.

# Solution
txt = "Hello World"
txt2 = txt.lower()
print(txt2)


# Task 5: Replace the character H with a J.

# Solution
txt = "Hello World"
txt3 = txt.replace("H", "J")
print(txt3)


# Task 6: Insert the correct syntax to add a placeholder for the age parameter.

# Solution
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
