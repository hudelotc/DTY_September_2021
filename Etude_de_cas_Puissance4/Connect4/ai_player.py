from player import Player
import copy


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """
	
    def __init__(self):
        self.name = "Mettez ici le nom de votre IA"

    
    def getColumn(self, board):
        
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
    
    def alphabeta(self, board, depth, alpha=0, beta=1000, maximizingPlayer=True):
        if depth == 0 or board.isFull() :
            return self.heuristic(board)
        
        if maximizingPlayer :
            value = -1
            for col in board.getPossibleColumns():
                child = copy.deepcopy(board)
                child.play(Player, col)
                
                value = max(value, self.alphabeta(child, depth-1, alpha, beta, False))
                
                if value >= beta :
                    break # beta cutoff 
                alpha = max(alpha, value)
            return value
        else:
            value = 1000
            for col in board.getPossibleColumns():
                child = copy.deepcopy(board)
                child.play(Player, col)
                
                value = min(value, self.alphabeta(child, depth-1, alpha, beta, True))
                if value <= alpha :
                    break #α cutoff 
                beta = min(beta, value)
            return value

    def heuristic(self, board):
        return 1
    
    def heuriList(self, List) :
        """
        Gives out the score for a list of four elements.
        """
        scoreGrid = [0, 1, 5, 50, 1000]
        scores = [0,0,0] # number of [empty, friend, foe] slots

        for slot in List:
            scores[slot] = scores[slot] +1

        if scores[-1] == 0 : # foe has no slot then points for me
            return scoreGrid[scores[1]]
        if scores[1] == 0 :  # I have no slot, then points for foe
            return -scoreGrid[scores[-1]]
        return 0