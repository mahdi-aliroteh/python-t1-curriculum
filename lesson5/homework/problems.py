import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
operating_systems = ["windows", "iOS", "android"]
print(operating_systems[len(operating_systems) - 1])
list.reverse(operating_systems)
print(operating_systems)

# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
school_subjects = ["science", "math", "english", "writing"]
print(school_subjects[1])
list.sort(school_subjects)
print(school_subjects)

# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
error_code = ["550", "173", "403","448", "829" ]
print(len(error_code))
err_403 = list.index(error_code, "403")
print(err_403)

# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
program_lang = ["HTML", "C++"]
print(program_lang[random.randint(0, (len(program_lang))-1)])
list.append(program_lang, "JavaScript")
print(program_lang)

# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
password = ["563399", "712873","364892", "465813", "750278", "170529"]
if len(password)%2 != 0: 
    password_len = int((len(password) - 1) / 2)
    print(password[password_len])
else:
    print("A list with an even number of elements does not have a middle")

password.pop(0)
print(password)
