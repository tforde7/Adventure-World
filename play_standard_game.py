from main_menu import MainMenu
from room import Room, RoomType
import random
from game_over import show_victory_message
import sys

MAIN_MENU = MainMenu()

class StandardGame:
    def __init__(self, player) -> None:
        self.player = player
        self.game_over = False

    def show_intro(self):
        print(
        """
        In a world torn by ancient prophecies, you awaken as a chosen hero in a small village.\n 
        The land of Etheria is fractured, its kingdoms scattered. A looming darkness threatens all. \n
        Your journey begins now, as you step forward to discover your destiny, wielding magic and courage\n 
        in a quest to restore balance and save Etheria from impending doom.\n\n

        The key to saving the land of Etheria lies in the power of the ancient Stone of Eternity.\n
        As you are about to embark on this dangerous quest to find the stone, you turn to say goodbye to \n
        your village one last time, fearing you may never return. You continue along \n
        the road and eventually you come to a fork in the road. \n
        """
    )

    def choose_direction(self):
        left_room, right_room = self.create_fork()

        while True:
            choice = input("Your choice: ")
            if choice.lower() == "left" or choice.lower() =="right":
                return left_room if choice.lower() == "left" else right_room
    
    def create_fork(self):
        left_room_type = random.choice(list(RoomType))
        while True:
            right_room_type = random.choice(list(RoomType))
            if right_room_type != left_room_type:
                break
    
        left_room = Room.create_room(left_room_type, self.player.choices)
        right_room = Room.create_room(right_room_type, self.player.choices)

        print("\nYou come to a fork in the road.")
        print(f"The road to your left leads to a {left_room.type.value}, \nand the road to your right leads to a {right_room.type.value}")
        print("Which way do you go? (left/right)")
        print("---------")
        return (left_room, right_room)
    
    def play_game(self):
        self.show_intro()
        while not self.game_over:
            choice = self.choose_direction()
            self.player.choices += 1
            print(f"\n{choice.description}")
            # Check if player wins based on win_probability
            win = random.random() < choice.win_probability
            if win:
                play_again = show_victory_message()
                if play_again == "1":
                    self.play_game()
                else:
                    sys.exit()
                
            else:
                print(f"\n You continue on past the {choice.type.value}")

        
