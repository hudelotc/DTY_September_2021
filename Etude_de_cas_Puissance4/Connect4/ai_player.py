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


    def heuristicList(self, array):
        pass


    def heuristicFull(self, array):
        res = 0
        for i in range(len(array)-3):
            res += self.heuristicList(array[i:i+4])
        return res

    def heuristic(self, board):
        evaluation = 0
        # col evaluation
        for col in board:
            evaluation += self.heuristicFull(col)
        # row evaluation
        for j in range(board.num_rows):
            row = board.getRow(j)
            evaluation += self.heuristicFull(row)
        # diag up evaluation
        for i in range(-2, 4):
            diag_up = board.getDiagonal(True, i)
            evaluation += self.heuristicFull(diag_up)
        # diag down evaluation
        for i in range(3, 9):
            diag_down = board.getDiagonal(False, i)
            evaluation += self.heuristicFull(diag_down)
        
        return evaluation
    

    