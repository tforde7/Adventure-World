class MainMenu:

    def __init__(self) -> None:
        pass

    def get_user_choice(self):
        return self.choice

    def show_menu(self):
        print("----------------------------")
        print ("Please choose an option:")
        print("----------------------------")
        print ("1. Create Player")
        print ("2. Play Standard Game")
        print ("3. Play AI Game")
        print ("4. Load Game")
        print ("5. Help")
        print ("6. Quit")
        print("----------------------------")
        self.choice = input("Your choice: ")




