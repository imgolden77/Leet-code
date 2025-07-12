class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        s_row=[set() for _ in range(9)]
        s_col=[set() for _ in range(9)]
        s_rec=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] not in s_row[i] and board[i][j] not in s_col[j] and board[i][j] not in s_rec[(i//3)*3+j//3]:
                    s_row[i].add(board[i][j])
                    s_col[j].add(board[i][j])
                    s_rec[(i//3)*3+j//3].add(board[i][j])
                else:
                    return False
        
        return True
        
        
            