from main_menu import MainMenu
from create_player import PlayerCreator
from openai import OpenAI
from image_generator import ImageGenerator
import os
from play_standard_game import StandardGame
from play_ai_game import show_play_ai_game
from options import show_options
from help import show_help
import sys


PLAYER_CREATOR = PlayerCreator()

OPENAI_CLIENT = None # Comment out this line when api key is inserted. Uncomment lines below
# os.environ['OPENAI_API_KEY'] = "Insert api key here" 
# OPENAI_CLIENT = OpenAI()

IMAGE_GENERATOR = ImageGenerator(OPENAI_CLIENT)

MAIN_MENU = MainMenu()

def handle_main_menu_choice(user_choice):
    if user_choice == '1':
        newPlayer = PLAYER_CREATOR.create_player()
        print("\nPlayer successfully created")
        PLAYER_CREATOR.show_player_info(newPlayer)
        while True:
            choice = input("\nWould you like to generate an avatar for your player? (y/n)")
            if choice == 'y':
                try:
                    avatar_prompt = PLAYER_CREATOR.create_prompt_for_avatar(newPlayer)
                    print("Generating player avatar...")
                    generated_image_response = IMAGE_GENERATOR.generate_image(avatar_prompt)
                    image = IMAGE_GENERATOR.convert_response_to_image(generated_image_response)
                    input("Avatar generated. Press enter to view..")
                    IMAGE_GENERATOR.save_image(image)
                    IMAGE_GENERATOR.display_image(image)
                except AttributeError:
                    print("API key not set")
                break
            elif choice == 'n':
                break
        show_menu()
    elif user_choice == '2':
        players = PLAYER_CREATOR.players
        if len(players) == 0:
            print("\nYou must first create a player.")
            show_menu()
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
        new_game = StandardGame(chosen_player)
        new_game.play_game()
    elif user_choice == '3':
        show_play_ai_game()
    elif user_choice == '4':
        show_help()
    elif user_choice == '5':
        sys.exit()

def show_menu():
    MAIN_MENU.show_menu()
    user_choice = MAIN_MENU.get_user_choice()
    handle_main_menu_choice(user_choice)


if __name__ == "__main__":

    show_menu()




