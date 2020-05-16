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
    sumx=0
    sumo=0
   
    """
    Returns player who has the next turn on a board.
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                sumx+=1
            elif board[i][j] == O:
                sumo+=1
    
   
    if sumo<sumx:
        return O
    else:
        return X
    



    
    



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act= []
    for i in range(3) :
        for j in range(3):
            if board[i][j] == EMPTY:
                act.append([i, j])
            
    return act
  
  


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    
    res=copy.deepcopy(board)
    res[action[0]][action[1]]= player(board)
    return res
    
 
        
     
    
   



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] != EMPTY:
            if board[i][0] == board[i][1]:
                if board[i][0] == board[i][2]:
                    return board[i][0]
        if board[0][i] != EMPTY:
            if board[0][i] == board[1][i]:
                if board[0][i] == board[2][i]:
                    return board[0][i]
        
    if board[1][1]!= EMPTY:
        if board[1][1] == board[0][0]:
            if board[1][1] == board[2][2]:
                return board[1][1]
    if board[1][1] != EMPTY:
        if board[1][1] == board[0][2]:
            if board[1][1] == board[2][0]:
                return board[1][1]
                
                
    return EMPTY
    
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) != EMPTY:
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
    if winner(board)== O:
        return -1
    return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if player(board) == X:
        best=(-1,-1)
        val=-1
        for act in actions(board):
            v=minv(result(board,act))
            if v == 1:
                best=act
                break
            if v > val :
                best = act
        return best
    if player(board) == O:
        best=(-1,-1)
        val=1
        for act in actions(board):
            v=maxv(result(board,act))
            if v == -1:
                best=act
                break
            if v < val :
                best = act
        return best
    
    
def maxv(board):
    
    if terminal(board):
        return utility(board)

    v = -1
    for act in actions(board):
        v=max(v,minv(result(board,act)))
        if v == 1:
            break
    return v
            
    


def minv(board):
    
    if terminal(board):
        return utility(board)
    
    v= 1
    for act in actions(board):
        v=min(v,maxv(result(board, act)))
        if v == -1:
            break
    return v
        
    
    
    
