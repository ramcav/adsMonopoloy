#!/usr/bin/python3


import board
import entity


class Game:
    def __init__(self) -> None:
        print("Welcom in adsMonopoly")

        self.new_party()

    def new_party(self):
        # prompt strings
        NB_PLAYER = "How many players are in the game?: "
        BOARD_SIZE = "On what board size do you want to play?: "

        # error messages
        NO_INT_SELECTION = "Enter a correct number"

        while True:
            try:
                nb_of_player = int(input(NB_PLAYER))
                break
            except ValueError:
                print(NO_INT_SELECTION)

        while True:
            try:
                board_size = int(input(BOARD_SIZE))
                break

            except ValueError:
                print(NO_INT_SELECTION)

        nb_of_tiles = ((board_size - 2) * 4) + 4

        print(f"You selected {nb_of_player} player.")
        print(f"You will play on a {board_size} x {board_size} board.")
        print(f"It contain : {nb_of_tiles} tiles")

        Party(nb_of_player, board_size)


class Party:
    def __init__(self, pl_nb: int, board_size: int) -> None:
        self.nb_of_player = pl_nb
        self.player_list = tuple(entity.Player('', i) for i in range(pl_nb))
        self.board = board.Board(board_size)

        # temporari variables for the player creation
        temp_name_list = []
        name = ''
        i = 0
        while i < self.nb_of_player:
            name = str(input(f"Enter the name of the player number {i}: "))

            if name not in temp_name_list:
                print(name)
                temp_name_list.append(name)
                self.player_list[i].name = name
                i += 1

            else:
                print("The name is alredy selected")

        # explicit removal of the variables
        del temp_name_list
        del name
        del i

        print("Have a good game:", end='')
        for i in self.player_list:
            print(f" {i.name}", end='')
        print()

    def play(self):
        self.turns = []

        while True:
            Turn(self.board, self.player_list)


class Turn:
    NB = 0

    def __init__(self,
                 board: board.Board,
                 player_list: tuple[entity.Player, ...]) -> None:
        self.turn_nb = Turn.NB

        Turn.NB += 1

        for nb_player, player in enumerate(player_list):
            if nb_player == player.priority:
                board.tiles_list[player.pos].when_walked(player)

    # turn checking player priority -> V
    # pass player pos to board -> V
    # board pass player to tile


def testing():
    print(board.Board(6))


if __name__ == '__main__':
    Game()
