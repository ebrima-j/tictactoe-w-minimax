"""
Tic Tac Toe Player
"""

from copy import deepcopy
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
    player = ''
    if board == initial_state():
        player = X
    else:
        Xcount = 0
        Ocount = 0
        for i in board:
            Xcount += i.count(X)
            Ocount += i.count(O)
            
        if Xcount <= Ocount:
            player = X
        else:
            player = O
        
    return player


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    i = 0;
    while (i < 3):
        j = 0
        while (j < 3):
            if board[i][j] == EMPTY:
                actions.append((i, j))
                j += 1
            else:
                j += 1
                continue
        i += 1

    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = deepcopy(board)
    p = player(board)

    if action in actions(board):
        newBoard[action[0]][action[1]] = p
        return newBoard
    else:
        raise Exception("Invalid Action")
        return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = ''

    #horizontally
    for i in board:
        if i[0] != EMPTY and (i[0] == i[1] and i[1] == i[2]):
            winner = i[0]

    #vertically
    #(0,0) (1,0) (2,0)
    if board[0][0] != EMPTY and (board[0][0] == board[1][0] and board[1][0] == board[2][0]):
        winner = board[0][0]
    #(0,1) (1,1) (2,1)
    if board[0][1] != EMPTY and (board[0][1] == board[1][1] and board[1][1] == board[2][1]):
        winner = board[0][1]
    #(0,2) (1,2) (2,2) 
    if board[0][2] != EMPTY and (board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        winner = board[0][2]

    #diagonally
    #(0,0) (1,1) (2,2)
    if board[0][0] != EMPTY and (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        winner = board[0][0]
    #(0,2)(1,1)(2,0)
    if board[0][2] != EMPTY and (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        winner = board[0][2]
        
    if winner == X:
        return X
    elif winner == O:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    over = False
        
    #if board is full
    if len(actions(board)) == 0:
        over = True
        
    #horizontally
    for i in board:
        if i[0] != EMPTY and (i[0] == i[1] and i[1] == i[2]):
            over = True

    #vertically
    #(0,0) (1,0) (2,0)
    if board[0][0] != EMPTY and (board[0][0] == board[1][0] and board[1][0] == board[2][0]):
        over = True
    #(0,1) (1,1) (2,1)
    if board[0][1] != EMPTY and (board[0][1] == board[1][1] and board[1][1] == board[2][1]):
        over = True
    #(0,2) (1,2) (2,2) 
    if board[0][2] != EMPTY and (board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        over = True

    #diagonally
    #(0,0) (1,1) (2,2)
    if board[0][0] != EMPTY and (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        over = True
    #(0,2)(1,1)(2,0)
    if board[0][2] != EMPTY and (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        over = True

    return over


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    utility = 0
        
    if winner(board) == X:
        utility = 1
    elif winner(board) == O:
        utility = -1
            
    return utility
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    def maxValue(board):
        if terminal(board):
            return utility(board)
        
        v = -math.inf
        for action in actions(board):
            v = max(v, minValue(result(board, action)))
            
        return v
        
    def minValue(board):
        if terminal(board):
            return utility(board)
        
        v = math.inf
        for action in actions(board):
            v = min(v, maxValue(result(board, action)))
            
        return v
        
    if terminal(board) == True:
        return None
    else:
        if player(board) == X:
            mx = maxValue(board)
                
            v = -math.inf
            for action in actions(board):
                v = max(v, minValue(result(board, action)))
                if v == mx:
                    return action
        elif player(board) == O:
            mn = minValue(board)
                    
            v = math.inf
            for action in actions(board):
                v = min(v, maxValue(result(board, action)))
                if v == mn:
                    return action
