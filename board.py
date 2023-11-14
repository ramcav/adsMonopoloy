import math

# Tile: tile class

class Card:
    def __init__(self):
        pass


class Tile:
    def __init__(self, name: str):
        self.name = name

    def when_walked(self, player: Player):
        pass

class Prison(Tile):
    def __init__(self):
        self.name = 'Prison'
        

class Train(Tile):
    def __init__(self):
        self.name = 'Train'

    
        

class StreetTile(Tile):

    # Dummy default player to init the owner
    DEFAULT_PLAYER = Player('none')

    def __init__(self, name: str, price: int):
        super.__init__(self, name)

        self.price = price

        self.houses = 0
        self.owner = Player('none')
        self.money_pool = 0

        self.rent = price//4

    # This method is triggered when a player stop on the tile
    def when_walked(self, player: Player):

        # first case: the tile does not have an owner
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

        # second case: the owner is on the tile
        elif self.owner is player:
            while True:
                desision = str(input("Do you want to buy a house [y/n]: "))
                if desision == "y":
                    if self.buy_house(player):
                        break
                    else:
                        break  # in the case of stubborn player
                elif desision == 'n':
                    break


        update_money_pool(player)


    # This method assign a tile to a player
    def buy_tile(self, player: Player):
        if self.owner is not StreetTile.DEFAULT_PLAYER:
            print("This tile is alredy owned")
            return 0
        
        if player.money >= self.price:
            player.money -= self.price
            self.owner = player
            return 1
        
        print("You don't have enough money")
        return 0


    # this method add a house to the tile (if lower than 3)
    def buy_house(self, house: int):
        if owner.money < self.price:
            print("You dont have enough money")
            return 0

        if self.houses >= 3:
            print("There is alredy 3 houses on this tile")
            return 0


        self.houses += 1
        return 1

    # Transfer the money of the tile to the owner OR 
    # transfer the "other player" money to the tile
    def update_money_pool(self, player: Player):
        if player is not self.owner:
            player.money -= self.rent * self.houses
            self.money_pool += self.rent * self.houses
        
        elif player is self.owner:
            player.money += self.money_pool
            self.money_pool = 0


    
    def __str__(self):
        return f'{self.properties}'
    
# Board: matrix, with each playable square storing a dictionary of information

class Board:
    def __init__(self, tiles_nb: int , tile_array: [Tile]):
        self.board = [[0 for _ in range(tiles_nb)] for _ in range(tiles_nb)]
        
        j = 0
        
        # populating the first collumn of the array
        for i in range(tiles_nb):
            self.board[i][0] = tile_array[j]
            #print(tile_array[j])
            j += 1


        for i in range(1,tiles_nb):
            self.board[tiles_nb-1][i] = tile_array[j]
            j += 1
            
        for i in range(tiles_nb-2, -1, -1):
            self.board[i][tiles_nb-1] = tile_array[j]
            j += 1
        
        for i in range(tiles_nb-2, 0, -1):
            self.board[0][i] = tile_array[j]
            j += 1
    
    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if isinstance(self.board[i][j], Tile):
                    print(f"{self.board[i][j].properties['name']}".ljust(15), end="")
                else:
                    print(" ".ljust(15), end="")
            print()


#class Board:
#    __init__(self, tiles_nb: int, tile_array: [Tile]):






class Player:
    def __init__(self, name):
        self.name = name
        self.houses = {}
        self.money = 0


def calculate_property_price(position, base_price=100, scale_factor=1.15):
    return math.ceil(base_price * (scale_factor ** position))



important_city_names_sorted_by_cost = [
    "Istanbul",
    "Mexico City",
    "Taipei",
    "Seoul",
    "Madrid",
    "Berlin",
    "Dubai",
    "Sydney",
    "London",
    "New York",
    "Copenhagen",
    "Paris",
    "Tokyo",
    "Hong Kong",
    "Geneva",
    "Singapore"
]

tile_array = []
for i, city in enumerate(important_city_names_sorted_by_cost):
    tile = {"name": city,
            "prices": calculate_property_price(i),
            "houses_available": 3,
            "current_houses": 0,
            "id": i}
    tile_array.append(Tile(tile))
    
board = Board(5, tile_array)

board.print_board()