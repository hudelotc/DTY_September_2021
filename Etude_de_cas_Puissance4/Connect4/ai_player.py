from player import Player
import copy
import numpy as np
from player import RandomPlayer
from game import Game


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """
	
    def __init__(self):
        self.name = "Mettez ici le nom de votre IA"

    
    def getColumn(self, board):
        #print("get")
        max_col = 0
        max_val = 0
        
        for col in board.getPossibleColumns():
            child = copy.deepcopy(board)
            child.play(Player, col)
            
            
            val = self.alphabeta(child, 3)
            if val > max_val:
                max_col = col
                max_val = val
        
        return max_col
    
    def alphabeta(self, board, depth, alpha=-np.inf, beta=np.inf, maximizingPlayer=True):
        if depth == 0 or board.isFull() :
            return self.heuristic(board)
        
        if maximizingPlayer :
            value = -np.inf
            for col in board.getPossibleColumns():
                child = copy.deepcopy(board)
                child.play(Player, col)
                
                value = max(value, self.alphabeta(child, depth-1, alpha, beta, False))
                
                if value >= beta :
                    return value # beta cutoff 
                alpha = max(alpha, value)
            return value
        else:
            value = np.inf
            for col in board.getPossibleColumns():
                child = copy.deepcopy(board)
                child.play(Player, col)
                
                value = min(value, self.alphabeta(child, depth-1, alpha, beta, True))
                if value <= alpha :
                    return value #alpha cutoff 
                beta = min(beta, value)
            return value

    def heuristic(self, board):
        return 1
    

if __name__ == '__main__':

    player1 = AIPlayer()
    player1.name = "p1"
    player2 = RandomPlayer()
    player2.name = "p2"
    game = Game(player1, player2, verbose=True)
    game.run()

    
    