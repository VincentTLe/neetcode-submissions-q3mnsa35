class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)

        
        
        for r in range(0,9):
            for c in range(0,9):
                square_index = (r//3) * 3 + (c//3)
                cell = board[r][c]
                if (cell == '.'):
                    continue
                if (cell in row[r]) or (cell in column[c]) or (cell in square[square_index]) :
                        return False 
                else:                   
                    row[r].add(cell)
                    column[c].add(cell)
                    square[square_index].add(cell)
        return True