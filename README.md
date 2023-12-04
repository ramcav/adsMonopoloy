# adsMonopoly: A Customizable Python Monopoly Game

## Introduction

adsMonopoly is a Python-based Monopoly game with a customizable board and enhanced gameplay features. It provides a fresh take on the classic Monopoly game with added flexibility and new mechanics.

## Requirements

- Python 3.x

## Installation Instructions

1. Clone/download the repository
2. Navigate to the project directory
3. Install requirements.txt if testing is desired.
4. Run `python main.py` to start the game

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

## Data Structures and Algorithms

### Data Structures

1. **Class-Based Structure**: Utilizing classes such as `Game`, `Player`, `Board`, and `Tile` allows for encapsulating complex functionalities and maintaining game state. This object-oriented approach simplifies code management and enhances readability, crucial for collaborative development.

2. **Tuples and Lists**: To manage collections such as `player_list`, tuples and lists offer efficient access and update operations. Tuples, being immutable, provide a reliable way to maintain the integrity of fixed data (like player order), while lists offer flexibility for dynamic data.

3. **Dictionaries**: In the `Player` class, dictionaries map properties to their respective number of houses. This choice facilitates quick lookups and updates, essential for real-time game actions like buying or upgrading properties.

4. **Stack**: In the `CardStack` there is a stack implementation that represents what in real life would be a stack of cards containing different penalties and bonifications. This allows for fast card retrieval, as the user is always getting a card from the head of the stack. Cards get reshuffled using `fisher_yates_shuffle` every time the stack gets empty.

### Algorithms

1. **Merge Sort**: (Time Complexity: O(n log n))

   - Used for ranking players based on their money. Merge Sort is chosen for its efficiency in sorting large datasets, crucial for maintaining an accurate and updated leaderboard after each turn.
   - Why Optimal: Merge Sort guarantees O(n log n) time complexity, making it highly efficient for sorting operations, even with a large number of players.

2. **Fisher-Yates shuffling**:

   - Used for sorting the card stack when it is repopulated.
   - Why Optimal: Fisher-Yates in its modern version uses random number generation to shuffle numbers in O(n) time complexity, which makes it really fast.

4. **Tile Management**:

   - The `when_walked` method in tile classes has a complexity of O(1), providing immediate feedback based on the game's current state.
   - Why Optimal: Instantaneous tile action resolution is crucial for a smooth and responsive gameplay experience, especially important in a turn-based game where player engagement is key.

5. **Board Initialization**:
   - Initializing the game board dynamically based on the chosen size involves calculating the number of tiles and strategically placing special tiles. This takes O(n) in general as this algorithm is reduced to generating the tiles, adding them to a list, doing transformations to it, and then using type casting to turn the final board into a tuple.
   - Why Optimal: This approach allows for a customizable and scalable board, catering to different game preferences and durations.
  
6. **Basic Stack Operations**:
   - For `Card` and `CardStack`, regular pop and append operations are carried away to allow users to take cards at random.
   - Why Optimal: This approach allows for users to always take O(1) time when grabbing a card as they are always doing so from the head.

### Complexity Analysis

- **Player Registration**: O(n), where n is the number of players. This linear complexity is due to the loop for player registration, ensuring that all players are accounted for without unnecessary overhead.
- **Gameplay Loop**: The main loop's complexity depends on the number of turns and player actions, striking a balance between complexity and game depth.
- **Tile Actions**: Generally, O(1), offering immediate feedback based on the current game state, is essential for player engagement and smooth game flow.

These data structures and algorithms were chosen to balance efficiency, scalability, and player engagement, forming the backbone of `adsMonopoly` and ensuring a robust and engaging gameplay experience.

## Group Members

Arian, Ricardo, Augustin, Peter
