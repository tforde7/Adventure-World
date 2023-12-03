# from main import show_menu
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

        weapon = input("Enter player race: (Suggestions: Sword, Axe, Bow etc.)\n")
        if len(weapon) <= 15:
            return weapon
        else:
            raise CharacterLengthExceeded("Maximum 15 characters")
    
    def create_player(self):
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
        newPlayer = Player(self.player_id, name, gender, race, weapon)
        self.players.append(newPlayer)
        self.player_id += 1
        return newPlayer

    
    def create_prompt_for_avatar(self, player):
        return f"""
        An avatar for a fantasy game. The character has the following attributes:
        Race: {player.race},
        Gender: {player.gender},
        Weapon: {player.weapon}
        """
    
    def generatePlayerAvatar(imageGenerator, prompt):
        imageGenerator.generateImage(prompt)
    



