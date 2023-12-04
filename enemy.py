from enum import Enum

class EnemyType(Enum):
    GIANT_SPIDER = 1
    ORC = 2
    DRAGON = 3

class Enemy:
    
    def __init__(self, enemy_type, health, strength) -> None:
        self.enemy_type = enemy_type
        self.health = health
        self.strength = strength

enemies = [
    Enemy(EnemyType.GIANT_SPIDER, 6, 6),
    Enemy(EnemyType.ORC, 4, 5),
    Enemy(EnemyType.DRAGON, 8, 8)
    ]

