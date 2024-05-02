# Task:  Write a program that uses a loop to display elements from a given list present at odd index position.

# Solution:
new_list = [10, 20, 30, 3, 55, 80, 90]

for i in range(len(new_list)):
    if i % 2 != 0:
        print(new_list[i])

