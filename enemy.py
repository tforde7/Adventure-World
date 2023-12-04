from enum import Enum

class EnemyType(Enum):
    GIANT_SPIDER = "Giant Spider"
    GOBLIN = "Goblin"
    DRAGON = "Dragon"

class Enemy:
    
    def __init__(self, enemy_type, health, strength) -> None:
        self.enemy_type = enemy_type
        self.health = health
        self.strength = strength

enemies = [
    Enemy(EnemyType.GIANT_SPIDER, 6, 6),
    Enemy(EnemyType.GOBLIN, 4, 5),
    Enemy(EnemyType.DRAGON, 8, 8)
    ]

