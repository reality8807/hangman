import random
import requests

url = 'https://random-word-api.herokuapp.com/word'
word = requests.get(url).json()[0]

guess = []
for _ in word:
    guess.append("_")

lives = 7
guessed_letters = []

while True:
    for blank in guess:
        print(blank, end="  ")

    guess_letter = input("\n\nMake your guess: ")

    if len(guess_letter) == 1 and guess_letter.isalpha():

        if guess_letter in guessed_letters:
            print(f"You have already guessed '{guess_letter}'. Try again")
            continue

        if guess_letter not in word:
            lives -= 1
            print("\nWrong guess")
            print(f"You have {lives} lives left.\n")
        else:
            start_pos = 0
            for letter in word:
                if guess_letter == letter:
                    pos = word.find(guess_letter, start_pos)
                    guess[pos] = guess_letter
                    start_pos += pos + 1

        if lives == 0:
            print("GAME OVER, you lose!")
            print(f"The word was {word}")
            break

        if ''.join(guess) == word:
            print("\nYOU WIN!")
            print(f"The word is {word}")
            break

        guessed_letters.append(guess_letter)

    else:
        print("Type a letter.")
