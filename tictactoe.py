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
    #Déclaration des compteurs de coups
    x_count = 0
    o_count = 0

    #Si le board est vide, c'est au tour de X
    if board == initial_state():
        return X

    #On compte le nombre de X et de O sur le board
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    
    #Si le nombre de X est supérieur au nombre de O, c'est au tour de O et inversement
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    
    # actions = X, O, or EMPTY
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #On vérifie que le coup est possible
    if action not in actions(board):
        raise Exception("Invalid action")

    #On récupère le joueur qui doit jouer
    current_player = player(board)

    #On copie le board
    board_copy = [row[:] for row in board]

    #On joue le coup
    board_copy[action[0]][action[1]] = current_player

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # On vérifie si un joueur a gagné
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]
    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #On vérifie si un joueur a gagné
    if winner(board) != None:
        return True
    
    #On vérifie si le board est plein
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
