import sys
from games import coin_flip, rock_paper_scissors, higher_or_lower

# TODO: Have this script act as a menu to start other games

while True:
    # Main game loop
    print("Welcome to the arcade!\n") # Intro message
    while True:
        cmd = input("What game would you like to play?\n").lower() # Get user input
        if cmd == "quit" or cmd == "exit": # Escape case to quit the game
            print("Goodbye!")
            sys.exit("Arcade closed.")

        if cmd == "coin flip":
            coin_flip.play()
        if cmd == "rock paper scissors" or cmd == "rps":
            rock_paper_scissors.play()
        if cmd == "higher or lower" or cmd == "higher/lower":
            higher_or_lower.play()
