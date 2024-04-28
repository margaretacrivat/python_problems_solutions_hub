# SETS

# Task 1: Use the correct method to add multiple items (more_fruits) to the fruits set.

# Solution
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)


# Task 2: Use the discard method to remove "banana" from the fruits set.

# Solution
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


# Task 3: Use the get method to print the value of the "model" key of the car dictionary.

# Solution
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))


# Task 4: Change the "year" value from 1964 to 2020.

# Solution
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2020


# Task 5: Add the key/value pair "color" : "red" to the car dictionary.

# Solution
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"


# Task 6: Use the pop method to remove "model" from the car dictionary.

# Solution
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")


# Task 7: Use the clear method to empty the car dictionary.

# Solution
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()
