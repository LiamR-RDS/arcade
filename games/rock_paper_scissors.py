import random

# fixed moves and win rules
MOVES = {"rock", "paper", "scissors"}
WIN_RULES = { # stored moves, avoid magic strings
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

#main game loop
def play():
    # variables
    player = 0
    opponent = 0

    print("Welcome to Rock Paper Scissors!\n")

    while True:
        move = input("Choose rock, paper, or scissors (type 'quit' to exit)\n> ").lower()

        if move in {"quit", "exit"}:
            print('Leaving "Rock Paper Scissors"...')
            return

        if move not in MOVES:
            print("Invalid move.")
            continue

        enemy = random.choice(tuple(MOVES))
        print(f"You played {move}.")
        print(f"Opponent played {enemy}.")

        if move == enemy:
            print(f"Tie! ({player}/{opponent})")
        elif WIN_RULES[move] == enemy:
            player += 1
            print(f"You win! ({player}/{opponent})")
        else:
            opponent += 1
            print(f"You lose! ({player}/{opponent})")

        print()

if __name__ == "__main__":
    play()
