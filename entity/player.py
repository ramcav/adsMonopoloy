class Player:
    def __init__(self, name: str, priority: int):
        self.priority = priority

        self.pos = 0

        self.name = name
        self.houses = {}
        self.money = 1000
