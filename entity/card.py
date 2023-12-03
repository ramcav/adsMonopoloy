import random
from . import player

class Card:
    def __init__(self, card_type: int):
        self.card_type = card_type
    
    def invoke(self, player: player.Player) -> int:
        if self.card_type == 0:
            prize = 100
            player.money += prize
            print(f"You've won the lottery! ${prize} have been added to your account!")
            return 0
        if self.card_type == 1:
            penalty = 100
            player.money -= penalty
            print("Oops! You forgot to pay your mortgage in time! 100 dollars have been subtracted from your account.")
            return 0 
        if self.card_type == 2:
            
            # Flag to check if an available tile
            # is found
            found = False
            
            # Add a house to the next available tile
            # with less than 3 houses
            for (tile, houses) in player.houses:
                if houses < 3:
                    print(f"You are really lucky! You just inherited a house at tile {tile}!")
                    player.houses[tile] += 1
                    tile.houses += 1
                    return 0
                
            # If no slot available, give the player money
            print("You are ver lucky! You just won $ 50 !")
            player.money += 50
            return 0
        else:
            return 1
                    
                    
class CardStack:
    def __init__(self, num_cards: int):
        cards = self.create_random_cards(num_cards)
        self.cards = self.shuffle(cards)
        self.stack = [card for card in self.cards]
        self.removed = []

    def create_random_cards(self, num_cards: int) -> [Card]:
        return [Card(random.randint(0, 2)) for _ in range(num_cards)]

    
    def take(self, player: player.Player) -> int:
        if len(self.stack) == 0:
            self.remake_stack()
        card = self.stack.pop()
        self.removed.append(card)
        card.invoke(player)
        
        return 0
    
    def remake_stack(self):
        cards = self.shuffle([card for card in self.removed])
        self.stack = [card for card in cards]
        
        return 0
        
    def shuffle(self, cards: []):
        
        # Fisher-Yates shuffle
        for i in range(len(cards) - 1, 0, -1):
            j = random.randint(0, i)
            cards[i], cards[j] = cards[j], cards[i]
        
        return cards

        
            
        
    