class Player:
    def __init__(self, name: str, priority: int):
        self.priority = priority

        self.pos = 0

        self.name = name
        
        # houses is a dict which stores
        # a reference to the tile as a key
        # and a value of the amount of houses
        # in such key
        
        self.houses = {}
        
        self.money = 0
