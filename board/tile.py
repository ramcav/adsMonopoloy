
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


class Prison(Tile):
    def __init__(self):
        self.name = 'Prison'
    
    def when_walked(self, board_size: int, player: entity.Player):
        pos_offset = board_size // 4
        # move the player backwards
        player.pos = board_size  % (2*player.pos - pos_offset)


class Train(Tile):
    def __init__(self):
        self.name = 'Train'
    
    def when_walked(self, board_size: int, player: entity.Player):
        pos_offset = board_size // 4
        # move the player forward
        player.pos = board_size % (player.pos + pos_offset)


class StreetTile(Tile):

    # Dummy default player to init the owner
    DEFAULT_PLAYER = entity.Player('none', -1)

    def __init__(self, name: str):
        super().__init__(name)

        # set by initialisation
        self.price = Tile.CAPITALES[name]
        self.rent = self.price//4
        self.owner = StreetTile.DEFAULT_PLAYER  # dummy player

        # changed by player interaction
        self.houses = 0
        self.money_pool = 0

    # This method is triggered when a player stop on the tile
    def when_walked(self, player: entity.Player):
        # first case: the Tile does not have an owner
        if self.owner is StreetTile.DEFAULT_PLAYER:
            while True:
                desision = str(input("Do you want to buy this Tile? [y/n]: "))
                if desision == "y":
                    if self.buy_tile(player):
                        break
                    else:
                        break  # Could be replace by an other player loan
                elif desision == "n":
                    break

        # second case: the owner is on the Tile
        elif self.owner is player:
            while True:
                desision = str(input("Do you want to buy a house [y/n]: "))
                if desision == "y":
                    if self.buy_house():
                        break
                    else:
                        break  # in the case of stubborn player
                elif desision == 'n':
                    break

        # third case: if any player walk an oned Tile
        elif (self.owner != StreetTile.DEFAULT_PLAYER) and (self.houses > 0):
            self.update_money_pool(player)

    # This method assign a tile to a player
    def buy_tile(self, player: entity.Player):
        if self.owner is not StreetTile.DEFAULT_PLAYER:
            print("This tile is alredy owned")
            return 0

        if player.money >= self.price:
            player.money -= self.price
            self.owner = player
            return 1

        print("You don't have enough money")
        return 0

    def __str__(self) -> str:
        return super().__str__()

    # this method add a house to the tile (if lower than 3)
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
            player.money -= self.rent * self.houses
            self.money_pool += self.rent * self.houses

        elif player is self.owner:
            player.money += self.money_pool
            self.money_pool = 0
