"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    if board == terminal:
        return X

    countX = 0
    for row in board:
        for element in row:
            if element == X:
                countX += 1
    countO = 0
    for row in board:
        for element in row:
            if element == O:
                countO += 1

    if countX > countO:
        return O
    else:
        return X


# print(player(initial_state()))

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set_of_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                set_of_actions.add((i, j))

    return set_of_actions


# print(actions(initial_state()))


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    # Create a manual copy of the board (since no imports allowed)
    new_board = [[board[row][col] for col in range(3)] for row in range(3)]

    if new_board[i][j] == EMPTY:
        new_board[i][j] = player(new_board)
        return new_board
    else:
        raise Exception("Invalid move: Cell is already occupied.")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:  # Check rows
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:  # Check columns
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None  # No winner found


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None  # Game is over, no action possible

    current_player = player(board)

    if current_player == X:
        best_value = float('-inf')
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action  # Return the best action for X
    else:
        best_value = float('inf')
        best_action = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action  # Return the best action for O


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
