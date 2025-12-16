import random
# The list called chib is the most important part of this code
chib = ["chibster","goobster", "shadi", "shadi jr", "shoo shoo", "lil chib", "strawberry", "blueberry", "Sweet Caramel Cookie", "Daydream Cookie", "Frosty Milk Cookie","Glich Cookie"]
# This is the space where all the functions are defined
def chib_words():
    chib_talk = input("Do you want chibster words: ")
    chib_talk_ans = str(chib_talk)
    if chib_talk_ans == "yes":
        for x in range(5):
            print(chib[random.randint(0, (len(chib))-1)])
    elif chib_talk_ans == "no":
        print("aww :(")
    else:
        print("Type yes or no in lowercase")
        chib_words()
def chib_words_1():
    chib_talk_1 = input("Do you want more chibster words: ")
    chib_talk_ans_1 = str(chib_talk_1)
    if chib_talk_ans_1 == "yes":
        for x in range(5):
            print(chib[random.randint(0, (len(chib))-1)])
    elif chib_talk_ans_1 == "no":
        print("aww :(")
    else:
        print("Type yes or no in lowercase")
        chib_words_1()
def add_word():
    chib_talk_2 = input("Do you want to create a chibster word: ")
    chib_talk_ans_2 = str(chib_talk_2)
    if chib_talk_ans_2 == "yes":
            new_word = input("Make sure it's chibsty: ")
            append_new_word = str(new_word)
            chib.append(append_new_word)
    elif chib_talk_ans_2 == "no":
        print("Okay")
    else:
        print("Type yes or no in lowercase")
        chib_words()
# Spaces represent a new section

chib_words()

print("Now, I will increase the chances of 3 random chibster words")
for q in range(2):
    chib.append((chib[random.randint(0, (len(chib))-1)]))
chib_words_1()

add_word()
chib_words_1()