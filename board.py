# Board: matrix, with each playable square storing a dictionary of information

class Tile:
    def __init__(self,properties):
        self.properties = properties
    
    def __str__(self):
        return f'{self.properties}'
        
    
            

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
                    print(f"{self.board[i][j].properties}".ljust(15), end="")
                else:
                    print("0".ljust(15), end="")
            print()

    
tile_array = [Tile(i) for i in range(20)]
board = Board(5, tile_array)

board.print_board()