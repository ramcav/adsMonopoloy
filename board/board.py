#!/usr/bin/python3

import data
import tile


class Board:
    def __init__(self, board_size=4):
        self.board_size = board_size
        self.tile_nb = board_size**2

        self.board_tiles = tuple(tile.StreetTile(i) for nbi, i in enumerate(data.capitales_dict) if nbi < self.tile_nb)

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
            to_display += self.str_format(self.board_tiles[counter].name)
            counter += 1

        to_display += '\n'

        for _ in range(counter, counter + self.board_size - 2):
            to_display += '|'
            to_display += self.str_format(self.board_tiles[counter].name)
            to_display += " " * (17 * (self.board_size - 2) - 1)
            to_display += '|'
            to_display += self.str_format(self.board_tiles[counter + 1].name)

            counter += 2
            to_display += '\n'

        to_display += '|'
        for _ in range(counter, counter + self.board_size):
            to_display += self.str_format(self.board_tiles[counter].name)
            counter += 1

        return to_display


def testing():
    print(Board(6))


if __name__ == '__main__':
    testing()
