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
        while True:
            name = input("Enter player name: ")
            if len(name) <= 20:
                return name
            else:
                raise CharacterLengthExceeded("Maximun 20 characters")

    def input_gender(self):

        gender = ''
        length_warning = ''
        while gender == '' or len(gender) > 12:
            gender = input(f"Enter player gender{length_warning}: ")
            length_warning = " (Maximun 12 charachters)"

        return gender

    def input_race(self):

        race = ''
        length_warning = ''
        while race == '' or len(race) > 12:
            print("Suggestions: Human, Elf, Dwarf")
            print("   ---   ")
            race = input(f"Enter player race{length_warning}: ")
            length_warning = " (Maximun 12 charachters)"

        return race

    def input_weapon(self):

        weapon = ''
        length_warning = ''
        while weapon == '' or len(weapon) > 12:
            print("Suggestions: Sword, Axe, Hammer")
            print("   ---   ")
            weapon = input(f"Enter player name{length_warning}: ")
            length_warning = " (Maximun 12 charachters)"
        return weapon
    
    def create_player(self):
        print("------")
        name = self.input_name()
        print("------")
        gender = self.input_gender()
        print('------')
        race = self.input_race()
        print("------")
        weapon = self.input_weapon()
        print('------')
        newPlayer = Player(self.player_id, name, gender, race, weapon)
        self.players.append(newPlayer)
        self.player_id += 1
        print("Generating player avatar...")
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
    



