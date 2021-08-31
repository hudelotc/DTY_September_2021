from player import Player
import copy


infty = float('inf')


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """
	
    def __init__(self, depth=3):
        self.name = "$ nepThune $"
        self.depth = depth

    
    def getColumn(self, board):
        """ Finds the column with the highess probability of winning

        Args:
            board (board.board): current game board

        Returns:
            int: column index between 0 and 6 (inclusive)
        """
        opt_col = None
        best_score = -infty
    
        for col in board.getPossibleColumns():
            child = copy.deepcopy(board)
            child.play(self.color, col)

            val = self.alphabeta(child, self.depth)
            if val > best_score:
                opt_col = col
                best_score = val
                
        return opt_col
  
    
    def alphabeta(self, board, depth=3, alpha=-infty, beta=infty, maximizingPlayer=True):
        """ Computes the alpha beta algorithm

        Args:
            board (board.board): current game board
            depth (int, optional): depth limit. 
                Defaults to 3.
            alpha (float, optional): minimum score that the maximum player is assured of.
                Defaults to -infty (worse case scenario for maximum player).
            beta ([type], optional): maximum score that the minimum player is assured of.
                Defaults to infty (worse case scenario for minimum player).
            maximizingPlayer (bool, optional): are we min or max player ?
                Defaults to True.

        Returns:
            int: the returned value of alphabeta algorithm
        
        Notes:
            See https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#Pseudocode for more info
        """
        if depth == 0 or board.isFull() :
            return self.heuristic(board)
        
        if maximizingPlayer:
            return self.maxvalue(board, depth, alpha, beta)
        else:
            return self.minvalue(board, depth, alpha, beta)


    def maxvalue(self, board, depth, alpha, beta):
        value = -infty
        for col in board.getPossibleColumns():
            child = copy.deepcopy(board)
            child.play(-self.color, col)
            
            value = max(value, self.alphabeta(child, depth-1, alpha, beta, False))
            
            if value >= beta:
                return value # beta cutoff 
            alpha = max(alpha, value)
        return value


    def minvalue(self, board, depth, alpha, beta):
        value = infty
        for col in board.getPossibleColumns():
            child = copy.deepcopy(board)
            child.play(self.color, col)
            
            value = min(value, self.alphabeta(child, depth-1, alpha, beta, True))
            if value <= alpha :
                return value #alpha cutoff 
            beta = min(beta, value)
        return value
   

    def heuristic(self, board):
        """ Compute the heuristic for alphabeta algorithm

        Args:
            board (board.board): current game board

        Returns:
            int: score of the current board
        """
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
        # diag up of length >= 4 have shift in range(-2, 4)
        for i in range(-2, 4):
            diag_up = board.getDiagonal(True, i)
            evaluation += self._heuristic_utils(diag_up)
        # diag down evaluation
        # diag down of length >= 4 have shift in range(3, 9)
        for i in range(3, 9):
            diag_down = board.getDiagonal(False, i)
            evaluation += self._heuristic_utils(diag_down)
        return evaluation
 

    def _heuristic_utils(self, array):
        """ Get the heuristic score for a given array (independently of its length is)

        Args:
            array (list): 

        Returns:
            int: score of the given array
        """
        res = 0
        for i in range(len(array)-3):
            res += self.getScore(array[i:i+4])
        return res


    def getScore(self, List):
        """ Get the heuristic score for an array of length 4

        Args:
            array (list): 

        Returns:
            int: score of the given array
        """
        scoreGrid = [0, 1, 7, 200, 10000]
        scores = [0,0,0] # number of [empty, friend, foe] slots

        for slot in List:
            scores[slot] = scores[slot] + 1

        if scores[-self.color] == 0: # foe has no slot then points for me
            return scoreGrid[scores[self.color]]
        if scores[self.color] == 0:  # I have no slot, then points for foe
            return -scoreGrid[scores[-self.color]]
        return 0
