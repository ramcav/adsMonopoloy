#!/usr/bin/python3

import data
from . import tile



class Board:
    def __init__(self, board_size=4):
        self.board_size = board_size
        self.tile_nb = board_size**2

        self.tiles_list = self.create_tiles(self.board_size)

    # Function to populate the board with
    # regular street tiles
    # and special tiles
    def create_tiles(self, board_size: int)->tuple:
         # Ensure frequency is at least 1
         # so we have at least one special tile
        
        freq = max(1, board_size // 5)
        special_tile_counter = 0
        tiles_temp_list = []
        j = 1

        for nbi, i in enumerate(data.capitales_dict):
            if nbi < self.tile_nb:
                if special_tile_counter == freq:
                    if j % 2 == 0:
                        special_tile = tile.Prison()
                    else:
                        special_tile = tile.Train()
                        
                    tiles_temp_list.append(special_tile)
                    special_tile_counter = 0
                    j += 1
                    
                else:
                    tiles_temp_list.append(tile.StreetTile(i))
                    special_tile_counter += 1

        return tuple(tiles_temp_list)
    
    

    def str_format(self, string) -> str:
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
            to_display += self.str_format(self.tiles_list[counter].name)
            counter += 1

        to_display += '\n'

        for _ in range(counter, counter + self.board_size - 2):
            to_display += '|'
            to_display += self.str_format(self.tiles_list[counter].name)
            to_display += " " * (17 * (self.board_size - 2) - 1)
            to_display += '|'
            to_display += self.str_format(self.tiles_list[counter + 1].name)

            counter += 2
            to_display += '\n'

        to_display += '|'
        for _ in range(counter, counter + self.board_size):
            to_display += self.str_format(self.tiles_list[counter].name)
            counter += 1

        return to_display


def testing():
    print(Board(6))


if __name__ == '__main__':
    testing()
