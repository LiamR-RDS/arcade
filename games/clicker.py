

def play():
    count = 0

    print("Welcome to clicker!")
    cmd = input('Type "Click" to click!\n>').lower()

    while True:
        if cmd in {"quit", "exit"}:
            return

        if cmd == "click":
            count += 1
            print(f"You clicked {count} times!")

        cmd = input('> ').lower()

if __name__ == "__main__":
    play()