# Tic-Tac-Toe with Monte Carlo Tree Search (MCTS) AI

This Python program simulates a game of Tic-Tac-Toe where a human player competes against an AI using **Monte Carlo Tree Search (MCTS)** to determine its moves. Below is a breakdown of the main components and how the code works.

## 1. Game Setup and Constants
   - `PLAYER_X` and `PLAYER_O` represent the two players.
   - `EMPTY` represents an empty cell on the board.
   - `WINNING_COMBINATIONS` is a list of tuples representing all possible winning lines on the board (rows, columns, diagonals).

## 2. MCTSNode Class
The `MCTSNode` class represents a state in the game and includes:
   - **Attributes**:
     - `board`: The current board state.
     - `current_player`: The player making a move (`X` or `O`).
     - `parent` and `children`: Relationships in the game tree, where `children` are possible moves from the current state.
     - `visits` and `wins`: Track the number of times the node was visited and its wins.
     - `untried_actions`: The possible moves from the current board state.
   - **Methods**:
     - `get_possible_moves`: Returns all empty positions on the board.
     - `make_move`: Simulates a move on the board.
     - `switch_player`: Switches between players `X` and `O`.
     - `is_terminal`: Checks if the game is over (win or draw).
     - `check_winner`: Checks if a player has won by examining `WINNING_COMBINATIONS`.

## 3. Monte Carlo Tree Search (MCTS) Process
The main logic of the AI uses MCTS to find the best move. The process includes:

   - **`mcts` function**: Runs MCTS simulations from the current node to select the optimal move.
     - Runs a loop of simulations (1000 iterations).
     - **`traverse`**: Navigates the tree to select a node to simulate.
     - **`expand`**: Expands the game tree by adding a child node for an unexplored action.
     - **`simulate`**: Plays random moves from the selected node until reaching a terminal state (win or draw).
     - **`backpropagate`**: Updates nodes in the path with the simulation result (win or draw).
   - **`select_best_child`**: Selects the child node with the highest potential for success using the Upper Confidence Bound (UCB1) formula.
   - **`best_move`**: Returns the move from the child node with the most visits, indicating it was frequently chosen as optimal during simulations.

## 4. Gameplay and Simulation Functions
   - **`simulate`**: Plays out a random game from a given node to the end.
   - **`is_terminal` and `check_winner`**: Helper functions to determine game-over conditions and check if any player has won.
   - **`print_board`**: Displays the current state of the board.

## 5. Main Game Loop
   - The **`main` function**:
     - Initializes an empty board and starts the game with `PLAYER_X`.
     - In each loop iteration:
       - If it’s the player’s turn (`X`), the player inputs a move.
       - If it’s the AI’s turn (`O`), MCTS is used to choose the best move.
     - The game ends when a player wins or the board is full (draw).

## Summary
This code simulates a Tic-Tac-Toe game between a human player and an AI using Monte Carlo Tree Search to make optimal moves for the AI. The player chooses moves manually, while the AI calculates the best move through thousands of MCTS simulations. The game ends with either a win for one of the players or a draw.
