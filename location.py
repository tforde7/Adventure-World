class Room:
    def __init__(self, name, description, ending=False):
        self.name = name
        self.description = description
        self.paths = {}
        self.ending = ending

    def add_paths(self, paths):
        self.paths.update(paths)

# Define the rooms
village = Room("Village", "You are in a lively village bustling with magical creatures.")
forest = Room("Enchanted Forest", "You've entered an enchanted forest with mystical trees.")
cave = Room("Dragon's Cave", "You stand at the entrance of a cave, home to a slumbering dragon.", ending=True)
castle = Room("Wizard's Castle", "You're inside a majestic castle filled with ancient tomes and magical artifacts.")
gemstone_room = Room("Chamber of the Gemstone", "You've found the ancient gemstone! Congratulations!", ending=True)
death1 = Room("Dark Abyss", "You fell into a dark abyss and perished.", ending=True)
death2 = Room("Haunted Swamp", "You got lost in the haunted swamp and met a grim fate.", ending=True)
# Define more rooms
river = Room("Mystic River", "You are standing by a tranquil river, its waters shimmer with magical energy.")
mountain = Room("Peak of Serenity", "You've reached the peak of a towering mountain with breathtaking views.")
beach = Room("Whispering Sands Beach", "You find yourself on a beach with sands that whisper secrets when touched.")
sky_palace = Room("Sky Palace", "You step into a palace floating among the clouds, a place of ethereal beauty.")
underwater_cavern = Room("Abyssal Cavern", "You've entered an underwater cavern, illuminated by glowing sea creatures.")
ruined_temple = Room("Forgotten Temple", "You stand amidst the ruins of an ancient temple, its history lost to time.")
volcano = Room("Volcanic Forge", "You're in the heart of a volcano, surrounded by molten lava and fiery heat.")
astral_plane = Room("Astral Plane Nexus", "You find yourself in a nexus of the astral plane, reality bending around you.")
ice_palace = Room("Frost Citadel", "You're inside a palace made entirely of ice, emanating an icy chill.")
timeless_garden = Room("Eternal Garden", "You've entered a garden frozen in time, its beauty eternal and untouched.")


# Define the connections between rooms
village.add_paths({'forest': forest, 'cave': cave, 'death1': death1, 'death2': death2})
forest.add_paths({'village': village, 'cave': cave, 'death1': death1, 'death2': death2})
cave.add_paths({'village': village, 'forest': forest, 'castle': castle, 'death1': death1, 'death2': death2})
castle.add_paths({'cave': cave, 'gemstone_room': gemstone_room, 'death1': death1, 'death2': death2})

# Set the starting room
current_room = village


class Location:
    def __init__(self) -> None:
        pass
