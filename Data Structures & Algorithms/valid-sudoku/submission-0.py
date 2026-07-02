class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == ".":
                    continue
                else:
                    for ignore, x in enumerate(row):
                        if val == x and ignore != j:
                            valid = False
                        
                    for col in range(9):
                        if board[col][j] == val and col != i:
                            valid = False

                    box_r = (i // 3) * 3
                    box_c = (j // 3) * 3
                    for x in range(box_r, box_r + 3):
                        for y in range(box_c, box_c + 3):
                            if (x, y) != (i, j) and board[x][y] == val:
                                valid = False
                
        return valid
