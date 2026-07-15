import random

words = ["apple", "cherry", "grape", "mango", "tiger"]

selected_word = random.choice(words)

hidden_word = []
for x in selected_word:
    hidden_word.append("_")

while "_" in hidden_word:
    print(" ".join(hidden_word))

    guess = input("Enter a letter: ")

    if guess in selected_word:
        print("correct")
    else:
        print("wrong")

    for index, letter in enumerate(selected_word):
        if letter == guess:
            hidden_word[index] = letter

print(" ".join(hidden_word))
print("You won!")