import random
import string

print(*"HANGMAN")

words = ['python', 'java', 'swift', 'javascript']

MAX_ATTEMPTS = 8
win = 0
loss = 0

while True:
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if choice == "play":
        word = random.choice(words)
        current_word = ['-'] * len(word)
        guessed_letters = []
        while MAX_ATTEMPTS > 0:
            print()
            print("".join(current_word))
            letter = input("Input a letter:")

            if len(letter) != 1:
                print("Please, input a single letter.")
                continue

            if letter not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
                continue

            if letter in guessed_letters:
                print("You've already guessed this letter.")
                continue

            guessed_letters.append(letter)

            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        current_word[i] = letter

                if current_word == list(word):
                    print(f"You guessed the word {word}!\nYou survived!")
                    win += 1
                    break
            else:
                MAX_ATTEMPTS -= 1
                print("That letter doesn't appear in the word.")
                continue

        if current_word != list(word):
            loss += 1
            print(f"You lost!")
        continue

    elif choice == "results":
        print(f"You won: {win} times.")
        print(f"You lost: {loss} times.")
        continue

    elif choice == "exit":
        break



