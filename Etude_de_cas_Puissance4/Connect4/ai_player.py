from player import Player
import copy


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """
	
    def __init__(self):
        self.name = "Mettez ici le nom de votre IA"

    
    def getColumn(self, board):
         # TODO(student): implement this!
        return 0
    
    def alphabeta(self, board, depth, alpha, beta, maximizingPlayer=True):
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
        return 0