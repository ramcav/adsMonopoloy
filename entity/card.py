from . import player


class Card:
    def __init__(self, card_type: int):
        # Initialize a card with a specific type
        self.card_type = card_type

    # This method has a time complexity of O(n) in the worst case(for loop),
    # where n is the number of houses the player owns.
    def invoke(self, player: player.Player) -> int:
        if self.card_type == 0:
            prize = 100
            player.money += prize
            print("You've won the lottery! ${Prize} have been added to your account!")
            return 0

        if self.card_type == 1:
            penalty = 100
            player.money -= penalty
            print(
                "Oops! You forgot to pay your mortgage in time! 100 dollars have been subtracted from your account."
            )
            return 0

        if self.card_type == 3:
            # Flag to check if an available tile is found
            found = False

            # Add a house to the next available tile with less than 3 houses
            # time complexity: O(n) for loop
            for tile, houses in player.houses:
                if houses < 3:
                    print(
                        f"You are really lucky! You just inherited a house at tile {tile}!"
                    )
                    player.houses[tile] += 1
                    tile.houses += 1
                    return 0

            # If no slot available, give the player money
            print("You are very lucky! You just won $ 50 !")
            player.money += 50
            return 0

        else:
            return 1


class CardStack:
    def __init__(self, cards: [Card]):
        # Initialize the card stack with shuffled cards
        self.cards = self.shuffle(cards)
        self.stack = [card for card in self.cards]
        self.removed = []


# Remove and invoke a card from the stack
# This method is O(1) as it pops the last item from a list
    def take(self, player: player.Player) -> int:
        card = self.stack.pop()
        self.removed.append(card)
        card.invoke(player)


# Shuffle and remake the stack from removed cards
 # The time complexity of this method depends on the shuffle algorithm used
# but a stack's time compexity tends to be O(n)
    def remake_stack(self):
        cards = self.shuffle([card for card in self.removed])
        self.stack = [card for card in cards]

    # This method is O(n) as it iterates through the list
    # and swaps each item with a random item
    # This is a Fisher-Yates shuffle
    def shuffle(self, cards: []):
        return cards
