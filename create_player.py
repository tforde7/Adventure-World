"""
This module defines a PlayerCreator class responsible for creating player instances.
It interacts with the Player class from the 'player' module to create player avatars with specific attributes
such as name, gender, race, and weapon. It allows users to assign stats (health, strength, and stamina) to the players.

The PlayerCreator class includes the following methods:
- input_name: Accepts player name input within a specified character limit.
- input_gender: Accepts player gender input within a specified character limit.
- input_race: Accepts player race input within a specified character limit.
- input_weapon: Accepts player weapon input within a specified character limit.
- create_player: Creates a new player with the provided details and adds stats to the player.
- create_prompt_for_avatar: Generates a prompt for a game avatar based on player attributes.
- generatePlayerAvatar: Calls an image generator to create an avatar based on a given prompt.
- add_stats_to_player: Allows users to allocate stat points (health, strength, stamina) to a player.
- get_details_input: Gathers player details using input methods and handles character length exceptions.
- show_player_info: Displays information about a player's attributes and stats.
- CharacterLengthExceeded: Custom exception class raised when input character limits are exceeded.
"""


from player import Player

class CharacterLengthExceeded(Exception):
      pass

class PlayerCreator:
    players = []
    player_id = 1

    def __init__(self) -> None:
        pass

    def input_name(self):
        name = input("Enter player name: ")
        if len(name) <= 20:
            return name
        else:
            raise CharacterLengthExceeded("Maximum 20 characters")

    def input_gender(self):

        gender = input("Enter player gender: ")
        if len(gender) <= 10:
            return gender
        else:
            raise CharacterLengthExceeded("Maximum 10 characters")

    def input_race(self):

        race = input("Enter player race: (Suggestions: Human, Elf, Dwarf etc.)\n")
        if len(race) <= 12:
            return race
        else:
            raise CharacterLengthExceeded("Maximum 12 characters")

    def input_weapon(self):

        weapon = input("Enter player weapon: (Suggestions: Sword, Axe, Bow etc.)\n")
        if len(weapon) <= 15:
            return weapon
        else:
            raise CharacterLengthExceeded("Maximum 15 characters")
    
    def create_player(self):

        name, gender, race, weapon = self.get_details_input()
        new_player = Player(self.player_id, name, gender, race, weapon)
        player_with_stats = self.add_stats_to_player(new_player)
        self.players.append(player_with_stats)
        self.player_id += 1
        return player_with_stats

    
    def create_prompt_for_avatar(self, player):
        return f"""
        An avatar for a fantasy game. The character has the following attributes:
        Race: {player.race},
        Gender: {player.gender},
        Weapon: {player.weapon}
        """
    
    def generatePlayerAvatar(imageGenerator, prompt):
        imageGenerator.generateImage(prompt)
    
    def add_stats_to_player(self, player):
        print("\nYou have 5 stat points to add. Choose wisely!")
        points_left = 5
        while points_left > 0:
            print("\nPlayer Stats:")
            print(f"Health: {player.health}")
            print(f"Strength: {player.strength}")
            print(f"Stamina: {player.stamina}")
            print("--------------------")
            print(f"\nYou have {points_left} points left.")
            print("1. Increase Health")
            print("2. Increase Strength")
            print("3. Increase Stamina")
            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                player.increase_health(1)
                points_left -= 1
            elif choice == '2':
                player.increase_strength(1)
                points_left -= 1
            elif choice == '3':
                player.increase_stamina(1)
                points_left -= 1
            else:
                print("Invalid choice. Please enter a valid option.")

        print("\nStats added successfully!")
        return player

    def get_details_input(self):
        print("------")
        while True:
            try:
                name = self.input_name()
                break 
            except CharacterLengthExceeded as exception:
                print(exception)
        print("------")
        while True:
            try:
                gender = self.input_gender()
                break 
            except CharacterLengthExceeded as exception:
                print(exception)        
        print('------')
        while True:
            try:
                race = self.input_race()
                break
            except CharacterLengthExceeded as exception:
                print(exception)
        print("------")
        while True:
            try:
                weapon = self.input_weapon()
                break
            except CharacterLengthExceeded as exception:
                print(exception)
        print('------')
        return (name, gender, race, weapon)

    def show_player_info(self, player):
        print("Player Info")
        print("---------------")
        print(f"Name: {player.name}")
        print(f"Gender: {player.gender}")
        print(f"Race: {player.race}")
        print(f"Weapon: {player.weapon}")
        print(f"\nHealth: {player.health}")
        print(f"Strength: {player.strength}")
        print(f"Stamina: {player.stamina}")
        print("---------------")




    



