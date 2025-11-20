# A game in which the player guesses a random number.
from random import randint


def play():

    MIN_INT : int = 1
    MAX_INT : int = 100

    guesses : int = 0 # Number of guesses the player has made
    num : int # Random number

    print("Welcome to Higher/Lower! Type \"quit\" or \"exit\" to quit.\n")

    # Main Loop
    while True:

        if guesses == 0: # Generate new number if the game just started.
            num = randint(MIN_INT,MAX_INT)

        guess = input(f"Guess a number ({MIN_INT}-{MAX_INT})\n> ")

        if guess == "quit" or guess == "exit":
            return
        
        if not guess.isdigit():
            print("Invalid input! Please enter a number or \"quit\" to quit.")
            continue

        guesses += 1
        if int(guess) < num:
            print("Higher!")
        if int(guess) > num:
            print("Lower!")
        if int(guess) == num:
            print(f"Correct! You took {guesses} guesses.")
            guesses = 0


if __name__ == "__main__":
    play()
