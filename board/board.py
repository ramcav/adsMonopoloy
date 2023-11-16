#!/usr/bin/python3

import data
from .tile import *

# Tile: tile class




class Card:
    def __init__(self):
        pass


    
# Board: matrix, with each playable square storing a dictionary of information

'''
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
'''

class Board:
    def __init__(self, board_size = 4):
        self.board_size = board_size
        self.tile_nb = board_size**2
    
        self.board_tiles = tuple(StreetTile(i) for nbi, i  in enumerate(data.capitales_dict) if nbi < self.tile_nb)
    
    
    def string_convert(self, string) -> str:
        buffer = 0
        if len(string) % 2:
            buffer = 1
        
        formated = ''
        str_buffer = -1 * (len(string) - 17) // 2

        formated += ' ' * str_buffer
        formated += string
        formated += ' ' * (str_buffer - buffer)
        formated += '|'
        
        return formated
    
    def __repr__(self) -> str:
        to_display = '|'
        
        counter = 0
        
        for _ in range(counter, self.board_size):
            to_display += self.string_convert(self.board_tiles[counter].name)
            counter += 1
            
        to_display += '\n'
            
        for _ in range(counter, counter + self.board_size - 2):
            to_display += '|'
            to_display += self.string_convert(self.board_tiles[counter].name)
            to_display += " " * (17 * (self.board_size - 2) - 1)
            to_display += '|'
            to_display += self.string_convert(self.board_tiles[counter + 1].name)
            
            counter += 2
            to_display += '\n'
        
        to_display += '|'
        for _ in range(counter, counter + self.board_size):
            to_display += self.string_convert(self.board_tiles[counter].name)
            counter += 1

        
        
        return to_display




def testing():
    print(Board(6))

if __name__ == '__main__':
    testing()