import data
import entity


class Tile:
    # a dictionary of capitals.
    # Time Complexity: Accessing this attribute is O(1).
    CAPITALES = data.capitales_dict

    def __init__(self, name: str):
        # Initializes a Tile with a name.
        # Time Complexity: O(1) as it's a simple assignment.
        self.name = name

    def when_walked(self, player: entity.Player):
        pass

    def __str__(self) -> str:
        # Time Complexity: O(1) as it returns a pre-defined attribute.
        return self.name


class Prison(Tile):
    def __init__(self):
        # Time Complexity: O(1) as it's a simple assignment.
        self.name = "Prison"

    def when_walked(self, player: entity.Player, board_size: int):
        # Method to define actions when a player walks on a Prison tile.
        # Moves the player backwards based on the board size.
        # Time Complexity: O(1) 
        pos_offset = board_size // 4  # Calculate the position offset

        # Move the player backwards and ensure it's within board limits.
        player.pos = (player.pos - pos_offset) % (((board_size - 2) * 4) + 4)

        # Print the new position of the player.
        print(f"Oops! You landed on the jail and moved back to {player.pos}")


class Train(Tile):
    def __init__(self):
        # Constructor to initialize a Train tile with a fixed name.
        # Time Complexity: O(1) as it's a simple assignment.
        self.name = 'Train'
    
    def when_walked(self, player: entity.Player, board_size: int):
        # Moves the player forward based on the board size.
        # Time Complexity: O(1) as the operations are basic arithmetic.
        pos_offset = board_size // 4
        player.pos = (player.pos + pos_offset) % (((board_size - 2) * 4) + 4)
        
        print(f"Congrats! You fell on the train and moved forward to {player.pos}")
    


class StreetTile(Tile):
    # Dummy default player to initialize the owner
    DEFAULT_PLAYER = entity.Player('none', -1)

    def __init__(self, name: str):
        # Time Complexity: O(1) dictionary lookup.
        super().__init__(name)
        self.price = Tile.CAPITALES[name]  # Lookup the price from a dictionary.
        self.rent = self.price // 4
        self.owner = StreetTile.DEFAULT_PLAYER  

        self.houses = 0
        self.money_pool = 0

    def when_walked(self, player: entity.Player, board_size = None):
        # Handles the logic when a player lands on this tile.
        # The complexity here is mainly O(1) except for the loops which depend on user input.
        
        # First case: the Tile does not have an owner
        if self.owner is StreetTile.DEFAULT_PLAYER:
            while True:
                decision = str(input("Do you want to buy this Tile? [y/n]: "))
                if decision == "y":
                    if self.buy_tile(player):
                        break
                    else:
                        break  # Could be replaced by another player interaction
                elif decision == "n":
                    break

        # Second case: the owner is on the Tile
        elif self.owner is player:
            while True:
                decision = str(input("Do you want to buy a house [y/n]: "))
                if decision == "y":
                    if self.buy_house():
                        break
                    else:
                        break  # In case of a stubborn player
                elif decision == 'n':
                    break

        # Third case: another player walks on an owned Tile
        elif (self.owner != StreetTile.DEFAULT_PLAYER) and (self.houses > 0):
            self.update_money_pool(player)


    # This method assigns a tile to a player
    # Time Complexity: O(1) because it is a simple assignment

    def buy_tile(self, player: entity.Player):
        # This method is for buying a tile. It checks if the tile is already owned.
        if self.owner is not StreetTile.DEFAULT_PLAYER:
            print("This tile is alredy owned")
            return 0

         # If not, it checks if the player has enough money to buy it.
        if player.money >= self.price:
            player.money -= self.price
            self.owner = player
            return 1

        print("You don't have enough money")
        return 0

    def __str__(self) -> str:
        return super().__str__()

    # this method adds a house to the tile (if lower than 3)
    def buy_house(self):
        if self.owner.money < self.price:
            print("You dont have enough money")
            return 0

        if self.houses >= 3:
            print("There is alredy 3 houses on this tile")
            return 0

        self.houses += 1
        return 1

    # Transfer the money of the tile to the owner OR
    # transfer the "other player" money to the tile
    def update_money_pool(self, player: entity.Player):
        if player is not self.owner:
            # If the player is not the owner rent is transferred from the player to the money pool
            player.money -= self.rent * self.houses
            self.money_pool += self.rent * self.houses

        elif player is self.owner:
            # If the player is the owner, the money pool is transferred to the player.
            player.money += self.money_pool
            self.money_pool = 0
