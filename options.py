class Options:

    def __init__(self, main_menu) -> None:
        self.main_menu = main_menu
        self.audio_enabled = False
        self.options = [
            "Audio Enabled"
        ]
    
    def showOptionsMenu(self):
        while True:
            print("\nOptions")
            print("-----------")
            print(f"{self.options[0]}: {self.audio_enabled}")
            print("-----------")
            print("1. Change")
            print("2. Save")
            while True:
                choice = input("\nYour choice: ")
                if choice == "1":
                    print("\nSelect option to change:")
                    for index, option in enumerate(self.options, start=1):
                        print(f"{index}. {option}")
                    print("-----")
                    while True:
                        option_choice = input("Your choice: ")
                        if option_choice == "1":
                            self.toggle_audio_enabled()
                            break
                elif choice == "2":
                    self.exit_options()
                    break
                else:
                    print("Invalid choice. Please select again.")
                break
                        
    def toggle_audio_enabled(self):
        self.audio_enabled = not self.audio_enabled
    
    def exit_options(self):
        self.main_menu.show_menu()
