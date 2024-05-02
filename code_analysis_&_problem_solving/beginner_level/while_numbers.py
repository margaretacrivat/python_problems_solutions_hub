# Task:  Write a python program that prints first 10 natural numbers using while loops.

# Solution:
n = 10
my_list = range(1, n + 1)

i = n - 1
my_index = 0

while my_index <= i:
    print(my_list[my_index])
    my_index = my_index + 1
