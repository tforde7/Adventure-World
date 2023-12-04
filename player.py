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
    


    

