import math

# Tile: tile class

class Tile:
    def __init__(self,properties):
        self.properties = properties
    
    def __str__(self):
        return f'{self.properties}'
    
# Board: matrix, with each playable square storing a dictionary of information       

class Board:
    def __init__(self, tiles, tile_array):
        self.board = [[0 for _ in range(tiles)] for _ in range(tiles)]
        
        j = 0
        
        for i in range(tiles):
            self.board[i][0] = tile_array[j]
            j += 1
            
        for i in range(1,tiles):
            self.board[tiles-1][i] = tile_array[j]
            j += 1
            
        for i in range(tiles-2, -1, -1):
            self.board[i][tiles-1] = tile_array[j]
            j += 1
        
        for i in range(tiles-2, 0, -1):
            self.board[0][i] = tile_array[j]
            j += 1
    
    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if isinstance(self.board[i][j], Tile):
                    print(f"{self.board[i][j].properties['name']}".ljust(15), end="")
                else:
                    print("0".ljust(15), end="")
            print()

class Player:
    def __init__(self):
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