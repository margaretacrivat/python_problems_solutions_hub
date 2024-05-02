# Task: Write a program that gives you the best report, price/amount and quantity for pizza.

# Hint: it's like doing a robot for a company that delivers pizza.
# For example: 50 /500 = 10, per 100 grams we pay 10 Ron.

# Solution:
number = int(input("How many pizza do you wish to compare? "))

for i in range(number):
    pizza = input("Input: pizza / price / quantity ")
    list_texts = pizza.split(" / ")
    name_pizza = list_texts[0]
    price = int(list_texts[1])
    quantity = int(list_texts[2])
    ratio = quantity/price
    print(f"The ratio is as follow: {ratio}")
