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
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    action
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board) is True:
        if utility(board) is 0:
            return None
        if utility(board) is 1:
            return X
        if utility(board) is -1:
            return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board) is 0 or 1 or -1:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if check_columns(board) == X or check_rows(board) == X or check_diagonals(board) == X:
        return 1
    if check_columns(board) == O or check_rows(board) == O or check_diagonals(board) == O:
        return -1
    else:
        return 0

def check_columns(board):
    """
    Returns X, O or None depending on the matching symbols found in the columns
    """
    for j in range (0,2):
        if board[0][j] == X and board[1][j] == X and board[2][j] == X:
            return X
        if board[0][j] == O and board[1][j] == O and board[2][j] == O:
            return O
        else:
            return None
 

def check_rows(board):
    """
    Returns X, O or None depending on the matching symbols found in the rows
    """
    for i in range (0,2):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        if board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
        else:
            return None

  

def check_diagonals(board):
    """
    Returns X, O or None depending on the matching symbols found in the diagonals
    """
    for d in range (0,2):
        if board[d][d] == X and board[d][d] == X and board[d][d] == X:
            return X
        if d != 1 and board[d][2-d] == X and board[1][1] == X and board[2-d][d] == X:
            return X
        if board[d][d] == O and board[d][d] == O and board[d][d] == O:
            return O
        if d != 1 and board[d][2-d] == O and board[1][1] == O and board[2-d][d] == O:
            return O

    return None

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    else:
        allowed_actions = actions(board)
        minimax_value = []

        if player(board) is X:
            for action in allowed_actions:
                minimax_value.append(max_value(result(board, action)))
                return allowed_actions[minimax_value.index(max(minimax_value))]

        else:
            for action in allowed_actions:
                minimax_value.append(min_value(result(board, action)))
                return allowed_actions[minimax_value.index(min(minimax_value))]

def max_value(board):
    """
    Returns the max value obtained from an action
    """
    v = -math.inf
    if terminal(board):
        return None
    
    else: 
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
            return v

def min_value(board):
    """
    Returns the min value obtained from an action
    """
    v = math.inf
    if terminal(board):
        return None

    else:
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
            return v