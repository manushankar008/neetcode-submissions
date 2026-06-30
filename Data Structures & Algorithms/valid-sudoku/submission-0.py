class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen=set()
            for j in range(len(board)):
                if board[i][j]!=".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        
        for i in range(len(board)):
            seen=set()
            for j in range(len(board)):
                if board[j][i]!=".":
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])
        
        row_start=0
        col_start=0
        row_end=3
        col_end=3

        while row_start<9:
            while col_start<9:
                seen=set()
                for i in range(row_start,row_end):
                    for j in range(col_start, col_end):
                        if board[i][j]!=".":
                            if board[i][j] in seen:
                                return False
                            seen.add(board[i][j])
                col_start+=3
                col_end+=3
            col_start=0
            col_end=3
            row_start+=3
            row_end+=3
        return True
            
                        

