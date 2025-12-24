# Problem 1
# Write a function that returns the number 42 and print the result.
def num_return():
    num = 42
    return num
print(num_return())


# Problem 2
# Write a function that returns "penguin" and print the result.
def lil_ping():
    pingu = "penguin"
    return pingu
print(lil_ping())

# Problem 3
# Create a variable for a fruit, then print it.
# Modify it inside a function and print it again.
fruit = "strawberry"
print(fruit)
def print_fruit():
    fruit = "yummy strawberry"
    return fruit
print(print_fruit())

# Problem 4
# Write a function that takes two parameters: first_name and last_name.
# The function should return a string that combines the first and last names separated by a space.
def input_name():
    first_name = input("What is your first name: ")
    first_name_1 = str(first_name)
    last_name = input("Please enter your last name: ")
    last_name_1 = str(last_name)
    full_name = (f"{first_name_1} {last_name_1}")
    return full_name
print(input_name())

    
# Problem 5
# Write a function called calculate_perimeter that takes two parameters: length and width.
# The function should return the perimeter of a rectangle (2 * (length + width)).
def calculate_perimeter():
    input_len = input("Please enter a number: ")
    input_len_1 = int(input_len)
    input_wid = input("Please enter a number: ")
    input_wid_1 = int(input_wid)
    perimeter = (2 * (input_len_1 + input_wid_1))
    return perimeter
print(calculate_perimeter())