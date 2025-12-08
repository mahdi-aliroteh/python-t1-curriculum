# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
print(names)
counter = names.count("Alex")
print(counter)


    




# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]
print(animals)
if "elephant" in animals:
    print("found elephant")
else:
    print("Elephant not found")


# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]
print(scores)
count = scores.count(100)
print(count)

# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
print(colors)
if "blue" in colors:
    index = colors.index("blue")
    print(index)
else:
    print("Blue not found")



# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]
print(temperatures)
temp_count = 0
for temp in temperatures:
    if temp < 0:
        temp_count += 1
print(temp_count)
