# Problem 1
# Use a while loop to print the word "Python" 4 times.
end = 0
while end < 4:
    print("Python")
    end = end + 1


# Problem 2
# Use a while loop to print the even numbers from 2 to 12 (inclusive).
end = 2
while end < 13:
    if end % 2 == 0:
        print(end)
    end = end + 1


# Problem 3
# Ask the user to input a positive number.
# Use a while loop to count up from 0 to that number (inclusive), printing each number.
input_num = input("Please enter a number: ")
input_int = int(input_num)
end = 0
while end <= input_int:
    print(end)
    end = end + 1


# Problem 4
# Ask the user to enter a starting number greater than 10.
# Use a while loop to count down by 5 each time until the number is less than 0.
def enter_num():
    input_num = input("Please enter a number greater than 10: ")
    input_int = int(input_num)
    if input_int <= 10:
        print("That number is 10 or less than 10. Please try again.")
        enter_num()
    else:
        return input_int
input_number = enter_num()
while input_number >= 0:
    print(input_number)
    input_number = input_number - 5


# Problem 5
# Create a list of your three favorite animals.
# Use a while loop to print each animal with the text "is awesome!" after it.
animal_list = ["Bunny", "Penguin", "Dog"]

end = 0
while end < len(animal_list):
    print(animal_list[end], "is awesome.")
    end = end + 1