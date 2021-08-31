from player import Player
import copy
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
            child.play(self.color, col)
            
            
            val = self.alphabeta(child, 3)
            if val > max_val:
                max_col = col
                max_val = val
        
        return max_col
    
    def alphabeta(self, board, depth=3, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=True):
        if depth == 0 or board.isFull() :
            return self.heuristic(board)
        
        if maximizingPlayer :
            value = -float('inf')
            for col in board.getPossibleColumns():
                child = copy.deepcopy(board)
                child.play(self.color, col)
                
                value = max(value, self.alphabeta(child, depth-1, alpha, beta, False))
                
                if value >= beta :
                    return value # beta cutoff 
                alpha = max(alpha, value)
            return value
        else:
            value = float('inf')
            for col in board.getPossibleColumns():
                child = copy.deepcopy(board)
                child.play(-self.color, col)
                
                value = min(value, self.alphabeta(child, depth-1, alpha, beta, True))
                if value <= alpha :
                    return value #alpha cutoff 
                beta = min(beta, value)
            return value

    def _heuristic_utils(self, array):
        res = 0
        for i in range(len(array)-3):
            res += self.heuriList(array[i:i+4])
        return res

    def heuristic(self, board):
        # print("enter heuristic")
        evaluation = 0
        # col evaluation
        for i in range(board.num_cols):
            col = board.getCol(i)
            evaluation += self._heuristic_utils(col)
        # row evaluation
        for j in range(board.num_rows):
            row = board.getRow(j)
            evaluation += self._heuristic_utils(row)
        # diag up evaluation
        for i in range(-2, 4):
            diag_up = board.getDiagonal(True, i)
            evaluation += self._heuristic_utils(diag_up)
        # diag down evaluation
        for i in range(3, 9):
            diag_down = board.getDiagonal(False, i)
            evaluation += self._heuristic_utils(diag_down)
        
        return evaluation
    
    def heuriList(self, List) :
        """
        Gives out the score for a list of four elements.
        """
        scoreGrid = [0, 1, 5, 50, float('inf')]
        scores = [0,0,0] # number of [empty, friend, foe] slots

        for slot in List:
            scores[slot] = scores[slot] +1

        if scores[-1] == 0 : # foe has no slot then points for me
            return scoreGrid[scores[1]]
        if scores[1] == 0 :  # I have no slot, then points for foe
            return -scoreGrid[scores[-1]]
        return 0

if __name__ == '__main__':

    player1 = AIPlayer()
    player1.name = "p1"
    player2 = RandomPlayer()
    player2.name = "p2"
    game = Game(player1, player2, verbose=True)
    game.run()

    
    
