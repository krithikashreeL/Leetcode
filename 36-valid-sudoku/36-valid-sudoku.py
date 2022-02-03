class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict = {}
        
        for i in range (0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] != ".":
                    row_check = str(board[i][j])+" found in row "+str(i)
                    col_check = str(board[i][j])+" found in col "+str(j)
                    box_check = str(board[i][j])+" found in box "+str((i//3))+str((j//3))
                    if (row_check not in dict) and (col_check not in dict) and (box_check not in dict):
                        dict[row_check] = row_check
                        dict[col_check] = col_check
                        dict[box_check] = box_check
                    else:
                        return False
        return True
                   