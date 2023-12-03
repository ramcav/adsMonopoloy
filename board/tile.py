import data
import entity

class Tile:
    CAPITALES = data.capitales_dict

    def __init__(self, name: str):
        self.name = name

    def when_walked(self, player: entity.Player):
        pass

    def __str__(self) -> str:
        return self.name

class Go(Tile):
    def __init__(self):
        super().__init__("Go")
        self.houses = False

    def when_walked(self, player: entity.Player, board_size: int):
        print("\nYou landed on Go!\n" + "-" * 24)

class Prison(Tile):
    def __init__(self):
        self.name = "Prison"
        self.houses = False
    
    def when_walked(self, player: entity.Player, board_size: int):
        pos_offset = board_size // 4
        # move the player backwards
        player.pos = (player.pos - pos_offset) % (((board_size - 2) * 4) + 4)

        print("\nOops! You landed on the jail and moved back to {}\n".format(player.pos) + "-" * 24)

class Train(Tile):
    def __init__(self):
        self.name = 'Train'
        self.houses = False
    
    def when_walked(self, player: entity.Player, board_size: int):
        pos_offset = board_size // 4
        side_length = board_size - 1

        # Move the player forward by the length of one side of the board
        player.pos = (player.pos + side_length) % (((board_size - 2) * 4) + 4)

        print("\nCongrats! You fell on the train and moved forward to {}\n".format(player.pos) + "-" * 24)

class StreetTile(Tile):
    # Dummy default player to init the owner
    DEFAULT_PLAYER = entity.Player('none', -1)

    def __init__(self, name: str):
        super().__init__(name)
        self.price = Tile.CAPITALES[name]
        self.rent = self.price // 4
        self.owner = StreetTile.DEFAULT_PLAYER  # dummy player
        self.houses = 0
        self.money_pool = 0

    def when_walked(self, player: entity.Player, board_size = None):
        print(f"\nYou landed on {self.name}.\n" + "-" * 24)

        # Tile does not have an owner
        if self.owner is StreetTile.DEFAULT_PLAYER:
            self.handle_tile_purchase(player)

        # The owner is on the Tile
        elif self.owner is player:
            self.handle_house_purchase(player)

        # Any player walk an owned Tile
        elif self.owner != StreetTile.DEFAULT_PLAYER and self.houses > 0:
            self.update_money_pool(player)

    def handle_tile_purchase(self, player: entity.Player):
        while True:
            decision = str(input(f"Do you want to buy this Tile? ($ {self.price}) [y/n]: "))
            if decision == "y":
                if self.buy_tile(player):
                    print(f"\nCongratulations! You now own {self.name}.\n" + "-" * 24)
                    break
                else:
                    print(f"\nUnable to purchase {self.name}.\n" + "-" * 24)
                    break  # Could be replace by another player loan
            elif decision == "n":
                print(f"\nYou chose not to purchase {self.name}.\n" + "-" * 24)
                break

    def handle_house_purchase(self, player: entity.Player):
        while True:
            decision = str(input("Do you want to buy a house on this Tile? [y/n]: "))
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

    def buy_tile(self, player: entity.Player):
        if self.owner is not StreetTile.DEFAULT_PLAYER:
            print("\nThis tile is already owned\n" + "-" * 24)
            return False

        if player.money >= self.price:
            player.money -= self.price
            self.owner = player
            return True

        print("\nYou don't have enough money\n" + "-" * 24)
        return False

    def __str__(self) -> str:
        return super().__str__()

    def buy_house(self):
        if self.owner.money < self.price:
            print("\nYou don't have enough money\n" + "-" * 24)
            return False

        if self.houses >= 3:
            print("\nThere are already 3 houses on this tile\n" + "-" * 24)
            return False

        self.houses += 1
        return True

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
