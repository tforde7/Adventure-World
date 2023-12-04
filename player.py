from enum import Enum

class FightResult(Enum):
    WIN = 1
    LOSE = 2

class RunAwayResult(Enum):
    SUCCESS = 1
    FAILURE = 2

class Player:
    def __init__(self, id, name, gender, race, weapon):
        self.id = id
        self.name = name
        self.gender = gender
        self.race = race
        self.weapon = weapon
        self.health = 5
        self.strength = 5
        self.stamina = 5
        self.choices = 1
    
    def increase_health(self, points):
        self.health += points
    
    def decrease_health(self, points):
        self.health -= points
    
    def increase_strength(self, points):
        self.strength += points
    
    def decrease_strength(self, points):
        self.strength -= points
    
    def increase_stamina(self, points):
        self.stamina += points
    
    def decrease_stamina(self, points):
        self.stamina -= points
    
    def is_dead(self):
        return self.health <= 0
    
    def fight(self, enemy):
        print("\nA fierce battle rages..")
        self.health -= enemy.strength
        return FightResult.WIN if self.health > 0 else FightResult.LOSE

    def run_away(self, enemy):
        print("\nYou attempt to run away..")
        self.stamina -= 3
        return RunAwayResult.SUCCESS if self.stamina > 0 else RunAwayResult.FAILURE
    


    

