Here's a README for your **Tic Tac Toe Player** project:

---

# Tic Tac Toe Player

This project is a Python implementation of a Tic Tac Toe game with an intelligent AI player using the minimax algorithm to make optimal moves.

## Features

- **Two-Player Game**: Supports moves for both players, "X" and "O".
- **Minimax Algorithm**: The AI evaluates optimal moves and always aims to play the best possible strategy.
- **Game Functions**: Includes functions to check the game status, evaluate possible moves, and determine the game's winner.

## Project Structure

- `initial_state()`: Sets up the initial game board with empty cells.
- `player(board)`: Determines which player has the next turn.
- `actions(board)`: Returns a set of all available actions on the board.
- `result(board, action)`: Returns the new board after a move is made.
- `winner(board)`: Checks if there is a winner.
- `terminal(board)`: Determines if the game is over.
- `utility(board)`: Assigns a score based on the game outcome (1 if "X" wins, -1 if "O" wins, 0 otherwise).
- `minimax(board)`: Uses the minimax algorithm to select the best move for the current player.

## Getting Started

### Requirements
- Python 3.x (no external libraries are needed).

### Running the Code

1. Clone or download this repository.
2. Place the code in a Python file, for example, `tictactoe.py`.
3. Run the file:

   ```bash
   python tictactoe.py
   ```

4. Modify the `player`, `result`, or `minimax` functions to make moves or simulate a game.

## How It Works

- **Minimax**: The AI recursively evaluates possible future moves and chooses the move that maximizes its chance of winning. If "X" is playing, it maximizes the outcome, while "O" minimizes it.
- **Game Logic**: Each function contributes to creating an intelligent game environment by managing turns, checking the game’s status, and evaluating the board's utility.

## Author

Roei Yanku
