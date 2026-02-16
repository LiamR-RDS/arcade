from random import randint

# fixed range
MIN_INT = 1
MAX_INT = 100

# main game loop
def play():
    # variables
    guesses = 0
    number = randint(MIN_INT, MAX_INT)

    print('Welcome to Higher / Lower! (type "quit" to exit)\n')

    while True:
        guess = input(f"Guess a number ({MIN_INT}-{MAX_INT})\n> ")

        if guess in {"quit", "exit"}:
            return

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guesses += 1
        value = int(guess)

        if value < number:
            print("Higher!")
        elif value > number:
            print("Lower!")
        else:
            print(f"Correct! You took {guesses} guesses.\n")
            guesses = 0
            number = randint(MIN_INT, MAX_INT)

if __name__ == "__main__":
    play()