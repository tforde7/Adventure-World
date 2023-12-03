from main_menu import show_main_menu
from player import Player

class PlayerCreator:
    players = []
    player_id = 1

    def __init__(self) -> None:
        pass

    def getName(self):
        name = ''
        length_warning = ''
        while name == '' or len(name) > 12:
            name = input(f"Enter player name{length_warning}: ")
            length_warning = " (Maximun 12 charachters)"
        return name

    def getGender(self):

        gender = ''
        length_warning = ''
        while gender == '' or len(gender) > 12:
            gender = input(f"Enter player gender{length_warning}: ")
            length_warning = " (Maximun 12 charachters)"

        return gender

    def getRace(self):

        race = ''
        length_warning = ''
        while race == '' or len(race) > 12:
            print("Suggestions: Human, Elf, Dwarf")
            print("   ---   ")
            race = input(f"Enter player race{length_warning}: ")
            length_warning = " (Maximun 12 charachters)"

        return race

    def getWeapon(self):

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
        name = self.getName()
        print("------")
        gender = self.getGender()
        print('------')
        race = self.getRace()
        print("------")
        weapon = self.getWeapon()
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
    



