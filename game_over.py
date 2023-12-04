def show_victory_message():
    print("Congratulations you found the Stone of Eternity!")
    print("You won the game!")
    print("Would you like to play again?")
    print("-----")
    print("1. Play again")
    print("2. Quit")
    print("-----")
    while True:
        choice = input("Your choice: ")
        if choice == "1" or choice == "2":
            return choice

def show_death_message():
    print("Bad luck you're dead!")
    print("You lost the game. :( )")
    print("Would you like to play again?")
    print("-----")
    print("1. Play again")
    print("2. Quit")
    print("-----")
    while True:
        choice = input("Your choice: ")
        if choice == "1" or choice == "2":
            return choice