#!/usr/bin/python3

import random
import board
import entity
from algos import merge_sort
from method import clear_screen

import os
import platform

from typing import Optional

class Game:
    def __init__(self) -> None:
        print("\nWelcome to adsMonopoly!\n")
        self.new_party()

    # Time Complexity: O(1)
    def new_party(self):
        
       # Prompt strings
        NB_PLAYER = "How many players are in the game?: "
        BOARD_SIZE = "On what board size do you want to play?: "

        # Error strings
        NO_INT_SELECTION = "Enter a correct number"

        # Time Complexity: O(1) (assuming the player enters a correct number)
        while True:
            try:
                nb_of_player = int(input(NB_PLAYER))
                if nb_of_player < 2:
                    print("You need at least 2 players to play.")
                else:
                    break
            except ValueError:
                print(NO_INT_SELECTION)
                
        # Time Complexity: O(1) (assuming the player enters a correct number)
        while True:
            try:
                board_size = int(input(BOARD_SIZE))
                break

            except ValueError:
                print(NO_INT_SELECTION)

        # Calculate the number of tiles on the board
        nb_of_tiles = ((board_size - 2) * 4) + 4

        # Print the game settings
        print(f"\nYou have selected {nb_of_player} player(s).")
        print(f"You will play on a {board_size} x {board_size} board with {nb_of_tiles} tiles.\n")

        # Start the game
        Party(nb_of_player, board_size)


class Party:
    def __init__(self, pl_nb: int, board_size: int) -> None:
        
        # initialize the game
        self.nb_of_player = pl_nb
        self.player_list = tuple(entity.Player('', i) for i in range(pl_nb))
        self.players_lost = []
        self.board = board.Board(board_size)
        
        # Temporary variables for the player registration
        temp_name_list = []
        name = ''
        i = 0
        
        # Player registration
        print("\nPlayer Registration\n" + "-" * 20)
        
        # Time Complexity: O(n) (n = nb_of_player)
        while i < self.nb_of_player:
            name = str(input(f"Enter the name of the player number {i}: "))

            # Check if the name is alredy selected
            if name not in temp_name_list:
                print(name)
                temp_name_list.append(name)
                self.player_list[i].name = name
                i += 1

            else:
                print("The name is alredy selected")

        # Explicitly delete of the temporary variables
        del temp_name_list
        del name
        del i

        # Start the game
        print("\nGame Start\n" + "-" * 10)
        print("Have a good game:", ', '.join(player.name for player in self.player_list))
        print("\n")

        self.play()
        print()

    def play(self):
        
        # Initialize the game
        # keep track of the turns and the current player
        self.turns = []
        current_player_index = 0

        # Time Complexity: O(n) (n = amount of turns for the game)
        while True:
            # Print the player list, sorted by money
            self.print_player_list(self.get_ranked_players())
            
            # Start a new turn
            Turn(self.board, self)
                
    # Time Complexity: O(n) (n = len(player_list))
    def print_player_list(self, player_list: Optional[tuple[entity.Player, ...]] = None):
        print("\nCurrent Player Rankings:\n" + "-" * 24)
        n = 1
        
        for player in player_list:
            if player.has_lost():
                print(f"Nº{n}. {player.name} has lost!", end='\n')
                continue
            current_tile = self.board.tiles_list[player.pos]
            if current_tile.houses != False:
                print(f"Nº{n}. {player.name} is on tile {player.pos} which has {current_tile.houses} houses (Money: {player.money})", end='\n')
                n += 1
            else:
                print(f"Nº{n}. {player.name} is on tile {player.pos} which has no houses (Money: {player.money})", end='\n')
                n += 1
        print()

    # Time Complexity: O(n log n) (n = len(player_list))
    # as merge sort is used
    def get_ranked_players(self):
        ranking = merge_sort(self.player_list, key=lambda x: x.money)
        return ranking

class Turn:
    NB = 0

    # Time Complexity: O(1)
    def __init__(self, board: board.Board, party:Party) -> None:
        self.turn_nb = Turn.NB
        Turn.NB += 1

        print(f"\n--- Start of Turn {self.turn_nb} ---\n")
        
        # Time Complexity: O(n) (n = len(player_list))
        for nb_player, player in enumerate(party.player_list):
                if player.has_lost():
                    continue
                # Cards given randomly
                if random.random() < 0.15:
                    print(f"{player.name} got a random card!")
                    board.card_stack.take(player)
                
                # Roll the dice
                self.roll_dice(player, board)
                if player.has_lost():
                    party.players_lost.append(player)
                    print(f"{player.name} lost!")
                    if len(party.players_lost) == party.nb_of_player - 1:
                        winner = next((player for player in party.player_list if not player.has_lost()), None)
                        print(winner.name + " won!")
                        exit()
                
    
        print(f"\n--- End of Turn {self.turn_nb} ---\n")  
        clear_screen()
        print("\nCurrent Board:\n" + "-" * 20)
        print()
        print(board) 
        current_player_index = 0 
        print("-" * 30 + "\n")

    # Time Complexity: O(1)
    def roll_dice(self, player: entity.Player, board: board.Board):
        # Roll the dice
        x = input((f"\n{player.name}'s turn: press enter to roll the dice: "))
        dice_outcome = random.randint(1, 6)

        print(f"\n{player.name} rolled a {dice_outcome}!")

        # Update the player position
        # Keep track of the previous position to check if the player has passed 'GO'
        player.prev_pos = player.pos  # Store current position as previous
        player.pos = (player.pos + dice_outcome) % (((board.board_size - 2) * 4) + 4)

        # Check if the player has passed 'GO'
        if player.prev_pos > player.pos:
            player.money += 200
            print(f"\nCongrats! {player.name} passed 'GO' and got 200$!\n")
            
            
        print(f"{player.name} landed on tile: {player.pos}")
        
        # Activste the tile action
        self.on_tile(player.pos, player, board)

    # Time Complexity: O(1) (depending on the tile action)
    def on_tile(self, tile_nb: int, player: entity.Player, board: board.Board):
        # Activate tile action
        board.tiles_list[tile_nb].when_walked(player, board.board_size)

if __name__ == '__main__':
    # Game()
    Game()