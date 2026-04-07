# Hangman game

import requests
import random

# Config
MAX_MISTAKES = 6


def fetch_random_word() -> str:
    """Fetch a random word from the API or return a fallback."""
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word", timeout=5)
        response.raise_for_status()
        words: list[str] = response.json()
        return words[0]
    except Exception as e:
        print(f"Error fetching word from API (possibly CORS): {e}")
        print("Using local fallback word.")
        return random.choice(["python", "arcade", "browser", "computer", "programming"])


def reveal_word(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play():
    word = fetch_random_word()  # fetch a random word from API or fallback
    guessed_letters: set[str] = set()  # use a set to track letters
    cur_mistakes = 0

    print("Welcome to Hangman!")
    print('Type "quit" or "exit" to return to the arcade.\n')

    while True:
        print(reveal_word(word, guessed_letters))
        print(f"Mistakes: {cur_mistakes}/{MAX_MISTAKES}")

        guess = input("Guess a letter: ").lower().strip()

        if guess in {"quit", "exit"}:
            return

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            cur_mistakes += 1
            print("Wrong guess!\n")
        else:
            print("Good guess!\n")

        if cur_mistakes >= MAX_MISTAKES:
            print(f"You lost! The word was: {word}")
            return

        if all(letter in guessed_letters for letter in word):
            print(f"You won! The word was: {word}")
            return


if __name__ == "__main__":
    play()
