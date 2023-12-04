from enum import Enum
from enemy import EnemyType
import random
import math

class RoomType(Enum):
    CAVE = "cave"
    FOREST = "forest"
    RIVER = "river"
    MOUNTAIN = "mountain"



ROOM_DESCRIPTIONS = {
    RoomType.CAVE: [
        "You find yourself in a dimly lit cave with mysterious markings on the walls.",
        "The cave echoes with the sound of dripping water and distant rumblings.",
        "You enter a cavernous space filled with glittering stalactites and stalagmites.",
        "A network of tunnels sprawls out before you, beckoning exploration.",
        "Faint light filters in from an opening, revealing a glimpse of an underground world."
    ],
    RoomType.FOREST: [
        "The forest teems with vibrant foliage and a chorus of chirping birds.",
        "Majestic trees loom overhead, their branches forming a natural canopy.",
        "Shafts of sunlight pierce through the thick foliage, creating a dappled pattern on the ground.",
        "A gentle breeze carries the scent of pine and earth through the air.",
        "You stumble upon a serene glade, a peaceful haven amidst the wilderness."
    ],
    RoomType.RIVER: [
        "Crystal-clear waters flow gracefully, reflecting the surrounding beauty.",
        "The river's gentle murmur provides a soothing soundtrack to your journey.",
        "You spot colorful fish darting among the rocks beneath the water's surface.",
        "Rippling currents carry fallen leaves downstream, painting a picturesque scene.",
        "Stepping stones offer a path across the river, inviting exploration on the other side."
    ],
    RoomType.MOUNTAIN: [
        "You stand atop a towering peak, surveying a breathtaking panorama below.",
        "Snow-capped peaks stretch as far as the eye can see, shrouded in tranquility.",
        "The mountain air is crisp and invigorating, filling you with a sense of awe.",
        "Rocky cliffsides provide a challenging yet rewarding climb for adventurers.",
        "A hidden cave entrance presents itself, promising secrets within the mountain's heart."
    ]
}

ENEMY_PROBABILITIES = {
    RoomType.CAVE: {
        EnemyType.DRAGON: 0.3,
        EnemyType.GIANT_SPIDER: 0.4,
        EnemyType.ORC: 0.1
    },
    RoomType.FOREST: {
        EnemyType.DRAGON: 0.1,
        EnemyType.GIANT_SPIDER: 0.2,
        EnemyType.ORC: 0.1
    },
    RoomType.MOUNTAIN: {
        EnemyType.DRAGON: 0.4,
        EnemyType.GIANT_SPIDER: 0.1,
        EnemyType.ORC: 0.1
    },
    RoomType.RIVER: {
        EnemyType.DRAGON: 0,
        EnemyType.GIANT_SPIDER: 0.2,
        EnemyType.ORC: 0.2
    }
}


class Room:
    def __init__(self, type, description, win_probability, enemy_probabilities):
        self.type = type
        self.description = description
        self.win_probability = win_probability
        self.enemy_probabilities = enemy_probabilities
    
    @staticmethod
    def create_room(room_type, player_choices):
        newRoom = Room(room_type, "", 0, {})
        random_description = ROOM_DESCRIPTIONS[room_type][random.randrange(5)]
        newRoom.description = random_description
        newRoom.enemy_probabilities = ENEMY_PROBABILITIES[room_type]

        # Calculate win probability using sigmoid function
        def sigmoid(x):
            return 1 / (1 + math.exp(-0.5 * (x - 5)))

        newRoom.win_probability = 0 if player_choices <= 2 else sigmoid(player_choices)
        return newRoom



