#!/usr/bin/python3

import data
import board.tile as tile
import entity.card as card


class Board:
    def __init__(self, board_size=4):
        self.card_stack = card.CardStack(24)
        self.board_size = board_size
        self.tile_nb = board_size**2

        # Comprehensions that generatre a list containing a list of street tiles
        
        tiles_list = [tile.Go()]
        for nbn, i in enumerate(data.capitales_dict):
            if nbn < self.tile_nb-1:
                tiles_list.append(tile.StreetTile(i))
            else:
                break

        # replacing a streettile by a prison tile
        tiles_list[self.board_size*3 - 3] = tile.Prison()

        # replacing 4 street tiles by train tiles
        abstract_middle = self.board_size//2
        for i in range(1, 5):
            side_middle = self.board_size * i - abstract_middle - i
            tiles_list[side_middle] = tile.Train()

        # converting linst in tuple of memory optimization
        self.tiles_list = tuple(tiles_list)

        # freeing the old list to releav the garbage colector
        del tiles_list


    # str_format center the name of the city in a | bounded standart sized area of 16 char
    def str_format(self, string1, houses) -> str:
        buffer = 0
        if houses != False:
            houses_str = f"({houses * 'H'})"
        else:
            houses_str = ''
            
        if len(string1) + len(houses_str) % 2:
            buffer = 1

        formated = ''
        str_buffer = -1 * (len(string1)+len(houses_str) - 17) // 2

        formated += ' ' * str_buffer
        formated += string1 + " " + houses_str
        formated += ' ' * (str_buffer - buffer)
        formated += '|'

        return formated

    def __repr__(self) -> str:
        # initialize `to_display` with |
        to_display = '|'        

        # separation of the 4 part of the table
        # 1. top_display:     the top of the board (contain 2 of the 4 corners)
        # 2. right_display:   the right part of the board (does not contain the corner)
        # 3. bottom_display:  the bottom part of the board  (contain 2 of the 4 corners)
        # 4. left_display:    the left part of the board (does not contain the corner)
        top_display = self.tiles_list[0:self.board_size]
        right_display = self.tiles_list[self.board_size: self.board_size*2 - 2]
        bottom_display = self.tiles_list[self.board_size * 2 - 2: self.board_size * 3 - 2]
        left_display = self.tiles_list[self.board_size*3 -2: self.board_size*4 - 4]

        # revers the right and bottom part of the bord for proper display
        # the bottom_display and left_display need to be reversed for--
        # --the correct "roatation" of the player on the board
        bottom_display = tuple(reversed(bottom_display))
        left_display = tuple(reversed(left_display))


        # print the top of the board
        for tile in top_display:
            to_display += self.str_format(tile.name, tile.houses)
        to_display += "\n"
        
        # print the 2 sides of the board
        for counter in range(len(right_display)):
            to_display += '|'
            to_display += self.str_format(left_display[counter].name, left_display[counter].houses)
            to_display += " " * (17 * (self.board_size - 2) - 1)
            to_display += '|'
            to_display += self.str_format(right_display[counter].name, right_display[counter].houses)
            to_display += '\n'

        # print the bottom part of the board (in revers order for continuity)
        to_display += '|'
        for tile in bottom_display:
            to_display += self.str_format(tile.name, tile.houses)
            
        return to_display
