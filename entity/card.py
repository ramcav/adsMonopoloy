import random
from . import player
from algos import fisher_yates_shuffle

# Card: parent class for all the cards
class Card:
    def __init__(self, card_type: int):
        self.card_type = card_type
        
    # Time Complexity: O(1)
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
            for tile, houses in player.houses.items():
                if houses < 3:
                    print(f"You are really lucky! You just inherited a house at tile {tile}!")
                    player.houses[tile] += 1
                    tile.houses += 1
                    found = True
                    return 0
                
            # If no slot available, give the player money
            if not found:
                print("You are ver lucky! You just won $ 50 !")
                player.money += 50
                found = False
                return 0
        else:
            return 1
        
        return 1
                    
# CardStack: class to handle the cards           
class CardStack:
    def __init__(self, num_cards: int):
        # Create the cards
        cards = self.create_random_cards(num_cards)
        self.cards = fisher_yates_shuffle(cards)
        self.stack = [card for card in self.cards]
        self.removed = []

    # Time Complexity: O(n) (n = num_cards)
    def create_random_cards(self, num_cards: int) -> list[Card]:
        return [Card(random.randint(0, 2)) for _ in range(num_cards)]

    # Time Complexity: O(1) 
    def take(self, player: player.Player) -> int:
        if len(self.stack) == 0:
            self.remake_stack()
        card = self.stack.pop()
        self.removed.append(card)
        card.invoke(player)
        
        return 0
    
    # Time Complexity: O(n) (n = len(removed))
    def remake_stack(self):
        cards = fisher_yates_shuffle([card for card in self.removed])
        self.stack = [card for card in cards]
        self.removed = []
        
        return 0
    
            
        
    