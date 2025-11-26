# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
user_test_int = input("Please enter your test score: ")
user_test = int(user_test_int)
user_test_int_1 = input("Please enter your second test score: ")
user_test_1 = int(user_test_int_1)
if user_test >= 50 and user_test_1 >= 50:
    print("You passed the test")
else:
    print("You failed the one of the tests or you failed both")



# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
user_lunch_input = input("Did you bring lunch (yes/no): ")
user_lunch = str(user_lunch_input)
user_water_input = input("Did you bring water (yes/no): ")
user_water = str(user_water_input)
if user_water == "yes" and user_lunch == "yes":
    print("You're ready for lunch")
elif user_water == "yes" or user_lunch == "yes":
    print("You're somewhat ready for lunch")
else:
    print("You're not ready for lunch")

# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
user_int_int = input("Please enter a number: ")
user_int = int(user_int_int)
if user_int >= 1 and user_int <= 10:
    print(f"The number {user_int} is in range")
else:
    print(f"The number {user_int} is out of range")
# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random
random_number = random.randint(1, 10)
random_guess_input = input("Please guess a number: ")
random_guess = int(random_guess_input)
if random_guess == random_number and random_number %2 == 0:
    print("Even match")
elif random_guess == random_number or random_number == 5:
   print("Nice try")
else:
   print("Nope")




# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
user_tell_int = input("Please enter a number: ")
user_tell = int(user_tell_int)
user_tell_int_1 = input("Please enter a second number: ")
user_tell_1 = int(user_tell_int_1)
if user_tell %5 == 0 and user_tell_1 %2 != 0:
    print(f"{user_tell} and {user_tell_1} are an interesting pair of numbers")
elif user_tell_1 %5 == 0 and user_tell %2 != 0:
    print(f"{user_tell_1} and {user_tell} are an interesting pair of numbers")
else:
    print(f"{user_tell} and {user_tell_1} are a boring pair of numbers")


    

