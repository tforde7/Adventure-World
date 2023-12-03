from main_menu import MainMenu
from create_player import PlayerCreator
from openai import OpenAI
from image_generator import ImageGenerator
import os
from play_standard_game import show_play_standard_game
from play_ai_game import show_play_ai_game
from options import show_options
from help import show_help
from load_game import show_load_game
import sys


PLAYER_CREATOR = PlayerCreator()

OPENAI_CLIENT = None # Comment out this line when api key is inserted. Uncomment lines below
# os.environ['OPENAI_API_KEY'] = "Insert api key here" 
# OPENAI_CLIENT = OpenAI()

IMAGE_GENERATOR = ImageGenerator(OPENAI_CLIENT)

MAIN_MENU = MainMenu()

class Room:
    def __init__(self, name, description, ending=False):
        self.name = name
        self.description = description
        self.paths = {}
        self.ending = ending

    def add_paths(self, paths):
        self.paths.update(paths)


def play_game():
    print("Welcome to the Quest for the Ancient Gemstone!")
    print("Your objective is to find the ancient gemstone that has the power to save the world.")
    print("However, along the way, there will be many dangers that you must avoid.\n")

    # Define the rooms
    village = Room("Village", "You are in a lively village bustling with magical creatures.")
    forest = Room("Enchanted Forest", "You've entered an enchanted forest with mystical trees.")
    cave = Room("Dragon's Cave", "You stand at the entrance of a cave, home to a slumbering dragon.", ending=True)
    castle = Room("Wizard's Castle", "You're inside a majestic castle filled with ancient tomes and magical artifacts.")
    gemstone_room = Room("Chamber of the Gemstone", "You've found the ancient gemstone! Congratulations!", ending=True)
    death1 = Room("Dark Abyss", "You fell into a dark abyss and perished.", ending=True)
    death2 = Room("Haunted Swamp", "You got lost in the haunted swamp and met a grim fate.", ending=True)

    # Define the connections between rooms
    village.add_paths({'forest': forest, 'cave': cave, 'death1': death1, 'death2': death2})
    forest.add_paths({'village': village, 'cave': cave, 'death1': death1, 'death2': death2})
    cave.add_paths({'village': village, 'forest': forest, 'castle': castle, 'death1': death1, 'death2': death2})
    castle.add_paths({'cave': cave, 'gemstone_room': gemstone_room, 'death1': death1, 'death2': death2})

    # Set the starting room
    current_room = village

    # Game loop
    while True:
        print("\n" + "=" * 30)
        print(f"{current_room.name}\n{current_room.description}")
        if current_room.ending:
            print("Game Over!")
            break
        print("Available paths:")
        for path in current_room.paths:
            print("- " + path.capitalize())
        print("Type 'quit' to exit.")

        # Player input
        direction = input("\nWhere do you want to go? ").lower()

        if direction == 'quit':
            print("Thanks for playing! Goodbye.")
            break

        if direction in current_room.paths:
            current_room = current_room.paths[direction]
        else:
            print("Invalid direction. Try again.")


    

def handle_main_menu_choice(user_choice):
    if user_choice == '1':
        newPlayer = PLAYER_CREATOR.create_player()
        avatar_prompt = PLAYER_CREATOR.create_prompt_for_avatar(newPlayer)
        generated_image_response = IMAGE_GENERATOR.generate_image(avatar_prompt)
        image = IMAGE_GENERATOR.convert_response_to_image(generated_image_response)
        input("Avatar generated. Press enter to view..")
        IMAGE_GENERATOR.save_image(image)
        IMAGE_GENERATOR.display_image(image)
    
    elif user_choice == '2':
        show_play_standard_game()
    elif user_choice == '3':
        show_play_ai_game()
    elif user_choice == '4':
        show_load_game()
    elif user_choice == '5':
        show_help()
    elif user_choice == '6':
        sys.exit()

def show_menu():
    # user_choice = show_main_menu()
    MAIN_MENU.show_menu()
    user_choice = MAIN_MENU.get_user_choice()
    handle_main_menu_choice(user_choice)


if __name__ == "__main__":

    show_menu()



