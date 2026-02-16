import random

# fixed odds
ODDS_HEADS = 0.5

# main game loop
def play():
    # variables 
    player = 0
    opponent = 0

    print("Welcome to Coin Flip!\n")

    while True:
        choice = input('Heads or tails? (type "quit" to exit)\n> ').lower()

        if choice in {"quit", "exit"}:
            print('Leaving "Coin Flip"...')
            return

        if choice not in {"heads", "tails"}:
            print('Invalid input. Use "heads" or "tails".')
            continue

        result = "heads" if random.random() < ODDS_HEADS else "tails"

        if choice == result:
            player += 1
            print(f"You win! ({player}/{opponent})")
        else:
            opponent += 1
            print(f"You lose! ({player}/{opponent})")


if __name__ == "__main__":
    play()