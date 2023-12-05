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

def get_victory_prompt():
    return "Congratulations! You found the Stone of Eternity! You won the game! Would you like to play again?"

def show_death_message():
    print("Bad luck, You lost the game. :( ")
    print("Would you like to play again?")
    print("-----")
    print("1. Play again")
    print("2. Quit")
    print("-----")
    while True:
        choice = input("Your choice: ")
        if choice == "1" or choice == "2":
            return choice

def get_death_prompt():
    return "Bad luck, you lost the game. Would you like to play again?"