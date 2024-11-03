import random
import math

# Constants
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '
WINNING_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
]

class MCTSNode:
    def __init__(self, board, current_player, parent=None):
        self.board = board
        self.current_player = current_player
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0
        self.untried_actions = self.get_possible_moves()

    def get_possible_moves(self):
        return [i for i in range(len(self.board)) if self.board[i] == EMPTY]

    def make_move(self, move):
        new_board = self.board[:]
        new_board[move] = self.current_player
        return new_board

    def switch_player(self):
        return PLAYER_X if self.current_player == PLAYER_O else PLAYER_O

    def is_terminal(self):
        return self.check_winner(PLAYER_X) or self.check_winner(PLAYER_O) or not self.get_possible_moves()

    def check_winner(self, player):
        return any(all(self.board[i] == player for i in combo) for combo in WINNING_COMBINATIONS)

def mcts(node):
    for _ in range(1000):  # Number of simulations
        leaf = traverse(node)
        result = simulate(leaf)
        backpropagate(leaf, result)
    return best_move(node)

def traverse(node):
    while node.untried_actions == [] and node.children:
        node = select_best_child(node)
    if node.untried_actions:
        return expand(node)
    return node

def expand(node):
    move = node.untried_actions.pop()
    new_board = node.make_move(move)
    child_node = MCTSNode(new_board, node.switch_player(), parent=node)
    node.children.append(child_node)
    return child_node

def select_best_child(node):
    return max(node.children, key=lambda n: n.wins / (n.visits + 1e-6) + math.sqrt(2 * math.log(node.visits + 1) / (n.visits + 1e-6)))

def simulate(node):
    board = node.board[:]
    player = node.current_player
    while not is_terminal(board):
        move = random.choice([i for i in range(len(board)) if board[i] == EMPTY])
        board[move] = player
        player = PLAYER_X if player == PLAYER_O else PLAYER_O
    if check_winner(board, PLAYER_X):
        return 1
    if check_winner(board, PLAYER_O):
        return -1
    return 0

def backpropagate(node, result):
    while node:
        node.visits += 1
        node.wins += result
        node = node.parent

def best_move(node):
    # Find the move with the most visits from the children
    best_child = max(node.children, key=lambda c: c.visits)
    return best_child.board.index(PLAYER_X if node.current_player == PLAYER_O else PLAYER_O)

def is_terminal(board):
    return check_winner(board, PLAYER_X) or check_winner(board, PLAYER_O) or not any(space == EMPTY for space in board)

def check_winner(board, player):
    return any(all(board[i] == player for i in combo) for combo in WINNING_COMBINATIONS)

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i + 3])

def main():
    board = [EMPTY] * 9
    current_player = PLAYER_X

    while not is_terminal(board):
        print_board(board)
        if current_player == PLAYER_X:
            try:
                move = int(input("Enter position (0-8): "))
                if move not in range(9) or board[move] != EMPTY:
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")
                continue
        else:
            root_node = MCTSNode(board, current_player)
            move = mcts(root_node)
        
        board[move] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

    if not check_winner(board, PLAYER_X) and not check_winner(board, PLAYER_O):
        print_board(board)
        print("It's a draw!")

if __name__ == "__main__":
    main()
