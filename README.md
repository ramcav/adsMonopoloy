# adsMonopoly: A Customizable Python Monopoly Game

## Introduction

adsMonopoly is a Python-based Monopoly game with a customizable board and enhanced gameplay features. It provides a fresh take on the classic Monopoly game with added flexibility and new mechanics.

## Requirements

- Python 3.x

## Installation Instructions

1. Clone/download the repository
2. Navigate to the project directory
3. Run `python main.py` to start the game

## How to Play

### Starting the Game

1. **Launch the Game**: Run `main.py` to start the game.
2. **Player Setup**: The game will prompt you to enter the number of players and their names. Follow the prompts to input this information.
3. **Board Setup**: You will be asked to choose the size of the board. The board size is customizable, allowing for a varied number of tiles.

### Gameplay

1. **Taking Turns**: Players take turns in a sequence. On each turn, a player will roll the dice by pressing Enter.
2. **Moving Around the Board**: The dice roll determines how many spaces the player moves forward on the board.
3. **Landing on Tiles**: Depending on the type of tile a player lands on, different actions will occur:
   - **Street Tiles**: Players have the option to purchase unowned properties or pay rent on owned properties.
   - **Prison Tile**: Landing on the Prison tile sends the player backward a certain number of spaces, calculated based on the board size.
   - **Train Tile**: Landing on the Train tile propels the player forward, moving them ahead on the board.
4. **Property Management**: Players can buy houses for their owned properties to increase rent.
5. **Player Interactions**: The game will prompt for decisions when players land on specific tiles, like buying properties or houses.

### Winning the Game

- The game continues until a winning condition is met (this can be customized based on your rules, such as a player going bankrupt or achieving a certain amount of wealth).

## Game Features

- Customizable board sizes
- Player name customization

## Code Structure

- `main.py`: The main game loop and game initialization.
- `tile.py`: Definitions of the different types of tiles on the board.
- `board.py`: Represents the game board. It initializes the board with a specified size, sets up the tiles (including special tiles like Prison), and handles the visual representation of the board.
- `player.py`: Defines the Player class. Each player in the game is an instance of this class, which tracks their properties, such as position on the board, money, and owned houses.
- `card.py`: Manages the cards used in the game. It includes the Card class for individual card actions and the CardStack class for handling the deck of cards.


## Group Members

Arian, Ricardo, Augustin, Peter
