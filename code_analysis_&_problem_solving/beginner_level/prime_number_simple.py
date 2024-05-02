# Task:  Write a program that displays only the prime numbers from a given number.

# Hint: first write a function which verify if the number is prime, then ask the user to input a number.

# Solution:
def is_prime(number):
    for i in range(2, (number//2)+1):
        if number % i == 0:
            return False
    return True


number = int(input("Input a number: "))

for i in range(1, number+1):
    if is_prime(i):
        print(f"The number {i} is prime!")


