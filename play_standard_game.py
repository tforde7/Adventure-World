from room import Room, RoomType
import random
from game_over import show_victory_message, show_death_message, get_death_prompt, get_victory_prompt
from enemy import enemies
import sys
from player import FightResult, RunAwayResult
from AI.generator_factory import GeneratorFactory

class StandardGame:
    def __init__(self, main_menu, player, audio_enabled) -> None:
        self.main_menu = main_menu
        self.player = player
        self.audio_enabled = audio_enabled
        self.game_over = False
        self.audio_generator = GeneratorFactory.get_audio_generator() if self.audio_enabled else None
        
    def show_intro(self):
        prompt = """
            In a world torn by ancient prophecies, you awaken as a chosen hero in a small village.\n 
            The land of Etheria is fractured, its kingdoms scattered. A looming darkness threatens all. \n
            Your journey begins now, as you step forward to discover your destiny, wielding magic and courage\n 
            in a quest to restore balance and save Etheria from impending doom.\n\n

            The key to saving the land of Etheria lies in the power of the ancient Stone of Eternity.\n
            As you are about to embark on this dangerous quest to find the stone, you turn to say goodbye to \n
            your village one last time, fearing you may never return. You continue along \n
            the road and eventually.. \n
            """
        if self.audio_enabled:
            self.generate_audio(prompt)

        print(prompt)

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

        prompt = f"You come to a fork in the road. The road to your left leads to a {left_room.type.value}, and the road to your right leads to a {right_room.type.value}. Which way do you go?"
        if self.audio_enabled:
            self.generate_audio(prompt)
        
        print("\nYou come to a fork in the road.")
        print(f"The road to your left leads to a {left_room.type.value}, \nand the road to your right leads to a {right_room.type.value}")
        print("Which way do you go? (left/right)")
        print("---------")
        return (left_room, right_room)
    
    def play_game(self):
        self.show_intro()
        while not self.game_over:
            direction_choice = self.choose_direction()
            self.player.choices += 1
            enemy_probabilities = direction_choice.enemy_probabilities
            found_enemy_type = None
            for enemy in enemy_probabilities:
                if random.random() < enemy_probabilities[enemy]:
                    found_enemy_type = enemy
                    break
            if found_enemy_type:
                for enemy in enemies:
                    if enemy.enemy_type == found_enemy_type:
                        found_enemy = enemy
                action_choice = self.handle_enemy(found_enemy)
                if action_choice == "1":
                    self.fight_enemy(found_enemy)
                else:
                    result = self.player.run_away(found_enemy)
                    if result == RunAwayResult.FAILURE:
                        while True:
                            if self.audio_enabled:
                                prompt = "You do not have enough stamina to run away. You must fight instead!"
                                self.generate_audio(prompt)
                            print("\nYou do not have enough stamina to run away!")
                            print("You must fight instead.")
                            action_choice = self.handle_enemy(found_enemy)
                            if action_choice == "1":
                                self.fight_enemy(found_enemy)
                                break
                    else:
                        if self.audio_enabled:
                            prompt = f"Success! You have escaped the {found_enemy.enemy_type.value}!"
                            self.generate_audio(prompt)
                        print(f"\nSuccess! You escaped the {found_enemy.enemy_type.value}!")

            print(f"\n{direction_choice.description}")
            # Check if player wins based on win_probability
            win = random.random() < direction_choice.win_probability
            if win:
                if self.audio_enabled:
                    prompt = direction_choice.description + get_victory_prompt()
                    self.generate_audio(prompt)
                play_again = show_victory_message()
                if play_again == "1":
                    self.play_game()
                else:
                    sys.exit()
                
            else:
                if self.audio_enabled:
                    prompt = direction_choice.description + f"You continue on past the {direction_choice.type.value}"
                    self.generate_audio(prompt)
                print(f"\nYou continue on past the {direction_choice.type.value}")
    
    def handle_enemy(self, enemy):
        if self.audio_enabled:
            prompt = f"You have encountered a {enemy.enemy_type.value}! Do you want to fight, or run away?"
            self.generate_audio(prompt)
        print(f"\n You have encountered a {enemy.enemy_type.value}!")
        print("Do you want to:")
        print("1. Fight")
        print("2. Run away")
        print("------")
        while True:
            choice = input("Your choice: ")
            if choice == "1" or choice == "2":
                return choice
    
    def fight_enemy(self, enemy):
        result = self.player.fight(enemy)
        if result == FightResult.LOSE:
            print(f"\nYou have been killed by the {enemy.enemy_type.value}!")
            death_prompt = get_death_prompt()
            if self.audio_enabled:
                prompt = f"You have been killed by the {enemy.enemy_type.value}!" + death_prompt
                self.generate_audio(prompt)
            play_again = show_death_message()
            if play_again == "1":
                self.play_game()
            else:
                sys.exit()
        else:
            print(f"\nYou have defeated the {enemy.enemy_type.value}!")
            if self.audio_enabled:
                prompt = f"You have defeated the {enemy.enemy_type.value}!"
                self.generate_audio(prompt)
    
    def generate_audio(self, prompt):
            generated_audio_response = self.audio_generator.generate_audio(prompt)
            self.audio_generator.save_audio(generated_audio_response)
            self.audio_generator.play_audio()
        
    




        
