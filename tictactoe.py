"""
Tic Tac Toe Player
"""

import math
import copy

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
    if terminal(board):
        return None

    Xcount = 0
    Ocount = 0

    for i in range(3):
        for j in range(3):
            if (board[i][j] == X):
                Xcount += 1
            if (board[i][j] == O):
                Ocount += 1

    if Xcount > Ocount:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                moves.add((i,j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not action:
        return board
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Forbidden move")
    
    result_board = copy.deepcopy(board)
    result_board[action[0]][action[1]] = player(board)
    
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_columns(board) == X or check_rows(board) == X or check_diagonals(board) == X:
        return X
    if check_columns(board) == O or check_rows(board) == O or check_diagonals(board) == O:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board) != 0 or len(actions(board)) == 0:
        return True
    else:
        return False


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
    

def check_columns(board):
    """
    Returns X, O or None depending on the matching symbols found in the columns
    """
    for j in range(3):
        if board[0][j] == X and board[1][j] == X and board[2][j] == X:
            return X
        if board[0][j] == O and board[1][j] == O and board[2][j] == O:
            return O
 

def check_rows(board):
    """
    Returns X, O or None depending on the matching symbols found in the rows
    """
    for i in range(3):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        if board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O


def check_diagonals(board):
    """
    Returns X, O or None depending on the matching symbols found in the diagonals
    """
    
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    else:
        if player(board) == X:
            return max_value(board)[1]
        elif player(board) == O:
            return min_value(board)[1]


def max_value(board):
    """
    Returns the action with max value
    """
    if terminal(board):
        return utility(board), None
    
    max_action = None
    v = -math.inf
    
    for action in actions(board):
        max = min_value(result(board, action))[0]
        if max > v:
            v = max
            max_action = action
    
    return v, max_action


def min_value(board):
    """
    Returns the action with min value
    """
    if terminal(board):
        return utility(board), None
   
    min_action = None
    v = math.inf
    
    for action in actions(board):
        min = max_value(result(board, action))[0]
        if min < v:
            v = min
            min_action = action
    
    return v, min_action