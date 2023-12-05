from play_standard_game import StandardGame
from create_player import PlayerCreator
from AI.image_generator import ImageGenerator
from options import Options
import sys

class MainMenu:

    def __init__(self) -> None:
        self.player_creator = PlayerCreator()
        self.image_generator = ImageGenerator(None)
        self.options = Options(self)

    def get_user_choice(self):
        return self.choice

    def show_menu(self):
        print("----------------------------")
        print ("Please choose an option:")
        print("----------------------------")
        print ("1. Create Player")
        print ("2. Play Standard Game")
        print ("3. Play AI Game")
        print ("4. Options")
        print ("5. Quit")
        print("----------------------------")
        while True:
            self.choice = input("Your choice: ")
            if self.choice in ["1","2","3","4","5"]:
                self.handle_choice(self.choice)
                break

    
    def handle_choice(self, choice):
        if choice == '1':
            self.handle_create_player()
        elif choice == '2':
            self.handle_play_standard_game()
        elif choice == '3':
            self.handle_play_ai_game()
        elif choice == '4':
            self.handle_options()
        elif choice == '5':
            sys.exit()
    
    def handle_create_player(self):
        newPlayer = self.player_creator.create_player()
        print("\nPlayer successfully created")
        self.player_creator.show_player_info(newPlayer)
        while True:
            choice = input("\nWould you like to generate an avatar for your player? (y/n)")
            if choice == 'y':
                try:
                    avatar_prompt = self.player_creator.create_prompt_for_avatar(newPlayer)
                    print("Generating player avatar...")
                    generated_image_response = self.image_generator.generate_image(avatar_prompt)
                    image = self.image_generator.convert_response_to_image(generated_image_response)
                    input("Avatar generated. Press enter to view..")
                    self.image_generator.save_image(image)
                    self.image_generator.display_image(image)
                except AttributeError:
                    print("API key not set")
                break
            elif choice == 'n':
                break
        self.show_menu()
    
    def handle_play_standard_game(self):
        players = self.player_creator.players
        if len(players) == 0:
            print("\nYou must first create a player.")
            self.show_menu()
        else:
            print("Choose a player:")
            for index, player in enumerate(players, start=1):
                print(f"{index}. {player.name}")
        while True:
            choice = input("\nYour choice: ")
            try:
                choice = int(choice)  # Convert input to an integer
                if 1 <= choice <= len(players):  # Check if the input is within the valid range
                    break
                else:
                    print("Invalid choice. Please select a number from the displayed options.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        chosen_player = players[choice - 1]
        audio_enabled = self.options.audio_enabled
        new_game = StandardGame(self, chosen_player, audio_enabled)
        new_game.play_game()

    def handle_play_ai_game(self):
        self.show_menu()

    def handle_options(self):
        self.options.showOptionsMenu()
        







