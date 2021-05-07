"""
Tic Tac Toe Player
"""
import copy
import math
import sys

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
    count = 0
    for row in board:
        for entry in row:
            if entry == EMPTY:
                count += 1
    # If the number of empty spaces is even, then it's O's turn
    if count % 2 == 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    to_return = set()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                to_return.add((i, j))

    return to_return


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)
    p = player(board)
    x = action[0]
    y = action[1]
    if new_board[x][y] != EMPTY:
        raise RuntimeError
    new_board[x][y] = p
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(0, 3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
    # Check columns
    for i in range(0, 3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        r = winner(board)
        if r == X:
            return 1
        elif r == O:
            return -1
        else:
            return 0
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        v = -sys.maxsize - 1
        next_action = None
        for action in actions(board):
            x = min_value(result(board, action))
            if x > v:
                v = x
                next_action = action
        return next_action
    else:
        v = sys.maxsize + 1
        next_action = None
        for action in actions(board):
            x = max_value(result(board, action))
            if x < v:
                v = x
                next_action = action
        return next_action


def max_value(board):
    v = -sys.maxsize - 1
    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = sys.maxsize + 1

    if terminal(board):
        return utility(board)

    for action in actions(board):
        if action is None:
            continue
        v = min(v, max_value(result(board, action)))
    return v
