# Player class
class Player:
    def __init__(self, name: str, priority: int):
        self.priority = priority

        self.pos = 0

        self.name = name
        
        self.has_completed_round = False
        
        self.houses = {}
        
        self.money = 1000

        self.prev_pos = 0

    def has_lost(self) -> bool:
        return self.money <= 0