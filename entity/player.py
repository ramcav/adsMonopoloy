class Player:
    def __init__(self, name: str, priority: int):
        self.priority = priority

        self.name = name
        self.houses = {}
        self.money = 0
        
        self.position = 0
