#!/usr/bin/python3

import random
import board
import entity


class Game:
    def __init__(self) -> None:
        # Constructor for Game class. Initializes a new game.
        # Time Complexity: O(1)
        print("Welcome in adsMonopoly")
        self.new_party()

    def new_party(self):
        # Starts a new party in the game.
        # Time Complexity: O(N) where N is the number of attempts to input valid data
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
        print(f"It contains: {nb_of_tiles} tiles")

        Party(nb_of_player, board_size)


class Party:
    def __init__(self, pl_nb: int, board_size: int) -> None:
        # It initializes players and the board
        # Time Complexity O(n) where n is the number of players due to the player creation loop
        self.nb_of_player = pl_nb
        self.player_list = tuple(entity.Player("", i) for i in range(pl_nb))
        self.board = board.Board(board_size)

        # temporary variables for the player creation
        temp_name_list = []
        name = ""
        i = 0
        while i < self.nb_of_player:
            name = str(input(f"Enter the name of the player number {i}: "))

            if name not in temp_name_list:
                print(name)
                temp_name_list.append(name)
                self.player_list[i].name = name
                i += 1

            else:
                print("The name is already selected")

        # explicit removal of the variables
        del temp_name_list
        del name
        del i

        print("Have a good game:", end="")
        for i in self.player_list:
            print(f" {i.name}", end="")

        self.play()  # test

        print()
        self.play()  # test

        print()

    def play(self):
        # Starts the play loop for the game
        # Time Complexity: it loops till a condition is met so it is not calculable
        self.turns = []

        while True:
            self.print_player_list(self.get_ranked_players())
            Turn(self.board, self.player_list)

    def print_player_list(self, player_list: tuple[entity.Player, ...] | None = None):
        # Prints the list of players.
        # Time Complexity: O(N) where N is the number of players.
        player_list = player_list or self.player_list
        for player in self.player_list:
            print(player.name, end=" ")

    def get_ranked_players(self):
        # Returns players ranked by money.
        # Time Complexity: O(n log n) due to merge sort
        ranking = merge_sort(self.player_list, key=lambda x: x.money)
        return ranking


def merge_sort(lst, key=lambda x: x):
    # Merge sort algorithm.
    # Time Complexity: O(N log N) where N is the length of the list because of the merge function.
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid], key)
    right_half = merge_sort(lst[mid:], key)

    return merge(left_half, right_half, key)


def merge(left, right, key):
    # Merges two lists in merge sort.
    # Time Complexity: O(N) where N is the total length of both lists because of the while loop.
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if key(left[left_index]) < key(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


class Turn:
    NB = 0

    def __init__(
        self, board: board.Board, player_list: tuple[entity.Player, ...]
    ) -> None:
        # Constructor for Turn class. Manages a single turn of a player.
        # Time Complexity: O(N) where N is the number of players
        self.turn_nb = Turn.NB
        Turn.NB += 1

        for nb_player, player in enumerate(player_list):
            if nb_player == player.priority:
                self.roll_dice(player, board)

    def roll_dice(self, player: entity.Player, board: board.Board):
        # Handles the dice roll action for a player.
        # Time Complexity: O(1) due to the random function
        x = input((f"\n{player.name}: press enter to roll the dice: "))
        dice_outcome = random.randint(1, 6)

        print(f"You got a {dice_outcome}!")

        player.pos = (player.pos + dice_outcome) % (((board.board_size - 2) * 4) + 4)
        print(f"You ended up on tile: {player.pos}")
        # walk on the tile
        self.on_tile(player.pos, player, board)

    def on_tile(self, tile_nb: int, player: entity.Player, board: board.Board):
        # Handles the action when a player lands on a tile.
        # Time Complexity: O(1) because it is a switch case
        board.tiles_list[tile_nb].when_walked(player, board.board_size)


def testing():
    # Testing function for the game.
    print(board.Board(8))


if __name__ == "__main__":
    # Main function to start the game.
    testing()
