import data
import entity


# Tile: parent class for all the tiles
class Tile:
    CAPITALES = data.capitales_dict

    def __init__(self, name: str):
        self.name = name

    def when_walked(self, player: entity.Player):
        pass

    def __str__(self) -> str:
        return self.name

# Go: Tile class
class Go(Tile):
    def __init__(self):
        # Call the parent constructor and set houses to False
        super().__init__("Go")
        self.houses = False
        
        # Dummy default player to init the owner
        self.owner = entity.Player("", -1)
        
    # Time Complexity: O(1)
    def when_walked(self, player: entity.Player, board_size: int):
        
        print("\nYou landed on Go!\n" + "-" * 24)

# Prison: Tile class
class Prison(Tile):
    def __init__(self):
        # Set the name and houses to False
        self.name = "Prison"
        self.houses = False
        
        # Dummy default player to init the owner
        self.owner = entity.Player("", -1)
    
    # Time Complexity: O(1)
    def when_walked(self, player: entity.Player, board_size: int):
        side_length = board_size - 1

        # Move the player backwards by the length of one side of the board
        player.pos = (player.pos - side_length) % (((board_size - 2) * 4) + 4)

        print("\nOops! You landed on the jail and moved back to {}\n".format(player.pos) + "-" * 24)

# Train: Tile class
class Train(Tile):
    def __init__(self):
        # Set the name and houses to False
        self.name = 'Train'
        self.houses = False
        
        # Dummy default player to init the owner
        self.owner = entity.Player("", -1)
    
    # Time Complexity: O(1)
    def when_walked(self, player: entity.Player, board_size: int):
        side_length = board_size - 1

        # Move the player forward by the length of one side of the board
        player.pos = (player.pos + side_length) % (((board_size - 2) * 4) + 4)

        print("\nCongrats! You fell on the train and moved forward to {}\n".format(player.pos) + "-" * 24)

# StreetTile: Tile class
class StreetTile(Tile):
    # Dummy default player to init the owner
    DEFAULT_PLAYER = entity.Player('none', -1)

    # Time Complexity: O(1)
    def __init__(self, name: str):
        # Call the parent constructor
        super().__init__(name)
        
        # Set the price, rent, owner, houses and money pool
        self.price = Tile.CAPITALES[name]
        self.rent = self.price // 2
        self.owner = StreetTile.DEFAULT_PLAYER  # dummy player
        self.houses = 0
        self.money_pool = 0

    # Time Complexity: O(1)
    def when_walked(self, player: entity.Player, board_size = None):
        print(f"\nYou landed on {self.name}.\n" + "-" * 24)

        # Tile does not have an owner
        if self.owner is StreetTile.DEFAULT_PLAYER:
            self.handle_tile_purchase(player)

        # The owner is on the Tile
        elif self.owner is player and self.money_pool == 0 and self.houses < 3:
            self.handle_house_purchase(player)

        # Any player walk an owned Tile
        elif self.owner != StreetTile.DEFAULT_PLAYER and self.houses > 0:
            self.update_money_pool(player)
        
        # Any player walk an owned Tile without houses
        elif self.owner != StreetTile.DEFAULT_PLAYER and self.houses == 0:
            print(f"\n{self.owner.name} owns this tile. You don't have to pay rent because there are no houses yet!.\n" + "-" * 24)

    # Time Complexity: O(1) (asuuming the player has enough money and either buys or doesn't buy the tile)
    def handle_tile_purchase(self, player: entity.Player):
        while True:
            decision = str(input(f"Do you want to buy this Tile? ($ {self.price}) [y/n]: "))
            if decision == "y":
                if self.buy_tile(player):
                    print(f"\nCongratulations! You now own {self.name}.\n" + "-" * 24)
                    break
                else:
                    print(f"\nUnable to purchase {self.name}.\n" + "-" * 24)
                    break
            elif decision == "n":
                print(f"\nYou chose not to purchase {self.name}.\n" + "-" * 24)
                break
    # Time Complexity: O(1) (assuming the player has enough money and either buys or doesn't buy the house)
    def handle_house_purchase(self, player: entity.Player):
        while True:
            decision = str(input(f"Do you want to buy a house on this Tile (${self.price//2})? [y/n]: "))
            if decision == "y":
                if self.buy_house():
                    print(f"\nYou bought a house on {self.name}. Total houses: {self.houses}\n" + "-" * 24)
                    break
                else:
                    print(f"\nUnable to buy a house on {self.name}.\n" + "-" * 24)
                    break  # in the case of a stubborn player
            elif decision == 'n':
                print(f"\nYou chose not to buy a house on {self.name}.\n" + "-" * 24)
                break
            
    # Time Complexity: O(1)
    # This method assign a tile to a player.
    def buy_tile(self, player: entity.Player):
        if self.owner is not StreetTile.DEFAULT_PLAYER:
            print("\nThis tile is already owned\n" + "-" * 24)
            return False

        if player.money >= self.price:
            player.money -= self.price
            self.owner = player
            player.tiles.append(self.name)
            return True

        print("\nYou don't have enough money\n" + "-" * 24)
        return False
    
    # Time Complexity: O(1)
    def __str__(self) -> str:
        return super().__str__()

    # Time Complexity: O(1)
    # This method add a house to the tile (if lower than 3)
    def buy_house(self):
        if self.owner.money < self.price // 2:
            print("\nYou don't have enough money\n" + "-" * 24)
            return False

        if self.houses >= 3:
            print("\nThere are already 3 houses on this tile\n" + "-" * 24)
            return False
        
        if self.houses == 0:
            self.owner.houses[self] = 1
        else:
            self.owner.houses[self] += 1
            
        self.houses += 1
        self.owner.money -= self.price // 2
        
        return True

    # Time Complexity: O(1)
    # Transfer the money of the tile to the owner OR
    # transfer the "other player" money to the tile
    def update_money_pool(self, player: entity.Player):
        if player is not self.owner:
            player.money -= self.rent * self.houses
            self.money_pool += self.rent * self.houses
            print(f"\n{player.name} paid rent of {self.rent * self.houses}.\n" + "-" * 24)
        elif player is self.owner:
            player.money += self.money_pool
            self.money_pool = 0
            if self.money_pool > 0:
                print(f"\n{player.name} collected {self.money_pool} from the money pool.\n" + "-" * 24)
