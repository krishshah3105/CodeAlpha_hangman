# Hangman Game
# Objective: Guess the hidden word one letter at a time.

import random

MAX_WRONG_GUESSES = 6
WORDS = ["apple", "banana", "python", "grape", "mango"]


def choose_random_word(words=None):
    available_words = words if words is not None else WORDS
    return random.choice(available_words)


def print_game_status(guessed_word, wrong_guesses, guessed_letters):
    print("\n================ HANGMAN STATUS ================")
    print("Word:", " ".join(guessed_word))
    print("Wrong guesses left:", MAX_WRONG_GUESSES - wrong_guesses)
    print("Letters guessed:", " ".join(guessed_letters))
    print("================================================")


def get_valid_guess(guessed_letters):
    while True:
        guess = input("Enter a letter to guess: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        return guess


def update_guessed_word(word, guessed_word, guess):
    matched = False
    for index, letter in enumerate(word):
        if letter == guess:
            guessed_word[index] = guess
            matched = True
    return matched


def play_hangman():
    print("=================================")
    print("      WELCOME TO HANGMAN")
    print("=================================")
    print(f"You have {MAX_WRONG_GUESSES} wrong guesses before the game is over.\n")

    word = choose_random_word()
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    wrong_guesses = 0

    while wrong_guesses < MAX_WRONG_GUESSES and "_" in guessed_word:
        print_game_status(guessed_word, wrong_guesses, guessed_letters)
        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if update_guessed_word(word, guessed_word, guess):
            print(f"Nice! The letter '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word correctly.")
            print("The word is:", word.upper())
            break

    if "_" in guessed_word:
        print("\nGame Over! You used all your guesses.")
        print("The correct word was:", word.upper())


if __name__ == "__main__":
    play_hangman()