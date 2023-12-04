#!/usr/bin/python3

import data
import board.tile as tile
import entity.card as card

# Board: tuple of tiles
class Board:
    def __init__(self, board_size=4):
        
        # initialize the card stack, board size and tile number
        self.card_stack = card.CardStack(24)
        self.board_size = board_size
        self.tile_nb = board_size**2

        # Initialize the tile list with the go tile
        tiles_list = [tile.Go()]
        
        # Populate the tile list with street tiles
        for nbn, i in enumerate(data.capitales_dict):
            if nbn < self.tile_nb-1:
                tiles_list.append(tile.StreetTile(i))
            else:
                break

        # Replacing one street tile by the prison tile
        tiles_list[self.board_size*3 - 3] = tile.Prison()

        # Replacing 4 street tiles by the train tiles
        abstract_middle = self.board_size//2
        for i in range(1, 5):
            side_middle = self.board_size * i - abstract_middle - i
            tiles_list[side_middle] = tile.Train()

        # Convert the list to a tuple
        self.tiles_list = tuple(tiles_list)

        # Free the memory of the list
        del tiles_list


    # Str_format to center the name of the city in a | bounded standart sized area of 16 char
    # Time Complexity: O(1)
    def str_format(self, string1, houses) -> str:
        
        buffer = 0
        
        # Add the houses to the string if there is any
        if houses != False:
            houses_str = f"({houses * 'H'})"
        else:
            houses_str = ''
            
        if len(string1) + len(houses_str) % 2:
            buffer = 1
            
        # Format the string
        
        formated = ''
        str_buffer = -1 * (len(string1)+len(houses_str) - 17) // 2

        formated += ' ' * str_buffer
        formated += string1 + " " + houses_str
        formated += ' ' * (str_buffer - buffer)
        formated += '|'

        return formated
    
    # Time Complexity: O(n) (n = len(self.tiles_list))
    def __repr__(self) -> str:
        # Initialize 'to_display' with |
        to_display = '|'        
        
        # Separation of the 4 part of the table
        # 1. top_display: the top of the board (contain 2 of the 4 corners)
        # 2. right_display: the right part of the board (does not contain the corner)
        # 3. bottom_display: the bottom part of the board (contain 2 of the 4 corners)
        # 4. left_display: the left part of the board (does not contain the corner)
        top_display = self.tiles_list[0:self.board_size]
        right_display = self.tiles_list[self.board_size: self.board_size*2 - 2]
        bottom_display = self.tiles_list[self.board_size * 2 - 2: self.board_size * 3 - 2]
        left_display = self.tiles_list[self.board_size*3 -2: self.board_size*4 - 4]

        # revers the right and bottom part of the bord for proper display
        # the bottom_display and left_display need to be reversed for--
        # --the correct "roatation" of the player on the board
        
        # Reverse the right part of the board for proper display
        # the bottom_display and left_display need to be reversed for--
        # --the correct "rotation" of the player on the board
        # Time Complexity: O(n) (n = len(right_display))
        bottom_display = tuple(reversed(bottom_display))
        left_display = tuple(reversed(left_display))


        # Print the top part of the board
        # Time Complexity: O(n) (n = len(top_display))
        for tile in top_display:
            to_display += self.str_format(tile.name, tile.houses)
        to_display += "\n"
        
        # Print the right and left part of the board
        # Time Complexity: O(n) (n = len(right_display))
        for counter in range(len(right_display)):
            to_display += '|'
            to_display += self.str_format(left_display[counter].name, left_display[counter].houses)
            to_display += " " * (17 * (self.board_size - 2) - 1)
            to_display += '|'
            to_display += self.str_format(right_display[counter].name, right_display[counter].houses)
            to_display += '\n'

        # Print the bottom part of the board
        # Time Complexity: O(n) (n = len(bottom_display))
        to_display += '|'
        for tile in bottom_display:
            to_display += self.str_format(tile.name, tile.houses)
            
        return to_display
