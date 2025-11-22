# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
user_input_str = input("Please enter an integer: ")
user_number = int(user_input_str)
if user_number % 2 == 0:
    print(f"{user_number} is an even number")
else:
    print(f"{user_number} is odd")
# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
user_input_day_of_week = input("Please enter a day of the week: ")
day_of_week = str(user_input_day_of_week)
if day_of_week == "saturday" or day_of_week == "sunday":
    print(f"{day_of_week} is a weekend")
elif day_of_week == "monday" or day_of_week == "tuesday" or day_of_week == "wednesday" or day_of_week == "thursday" or day_of_week == "friday":
    print(f"{day_of_week} is a weekday")
else:
    print(f"{day_of_week} is not a day of the week")


# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
import random
number_guess = random.randint(1, 10)
#print(number_guess)
user_input_num_guess = input("Please guess a number: ")
user_enter = int(user_input_num_guess)
if user_enter == number_guess:
    print("how did you guess the number!!!")
else:
    print(f"the number was {number_guess} try again")



# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
user_input_str1 = input("Please enter an integer: ")
user_number1 = int(user_input_str1)
if user_number1 % 2 == 0 and user_number1 > 10:
    print(f"{user_number1} is a big even number")
else:
    print(f"{user_number1} does not meet the criteria")


# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
user_input_num_1 = input("Please enter a number: ")
user_number_2 = int(user_input_num_1)
user_input_num_2 = input("Please enter a second number: ")
user_number_3 = int(user_input_num_2)
if user_number_2 > user_number_3:
    print(f"{user_number_2} is bigger than {user_number_3} ")
elif user_number_3 > user_number_2:
    print(f"{user_number_3} is bigger than {user_number_2}")
else:
    print(f"{user_number_2} and {user_number_3} are equal")
