# LISTS

# Task 1: Print the second item in the fruits list.

# Solution
fruits = ["apple", "banana", "cherry"]
print(fruits[1])


# Task 2: Change the value from "apple" to "kiwi", in the fruits list.

# Solution
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits[0])


# Task 3: Use the append method to add "orange" to the fruits list.

# Solution
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)


# Task 4: Use the insert method to add "lemon" as the second item in the fruits list.

# Solution
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
print(fruits)


# Task 4: Use the remove method to remove "banana" from the fruits list.

# Solution
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)


# Task 5: Use negative indexing to print the last item in the list.

# Solution
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])


# Task 6: Use a range of indexes to print the third, fourth, and fifth item in the list.

# Solution
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


# Task 6: Use the correct syntax to print the number of items in the list.

# Solution
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
