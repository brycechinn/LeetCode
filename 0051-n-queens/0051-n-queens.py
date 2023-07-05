class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # approach: backtracking DFS, three hashsets for cols, 
        # positive diagonals (r + c), negative diagonals (r - c)
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        cols = set()
        pos_diags = set() # r + c
        neg_diags = set() # r - c
        
        def dfs(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if (c in cols or 
                    r + c in pos_diags or 
                    r - c in neg_diags):
                    continue
            
                # place queen
                board[r][c] = 'Q'
                cols.add((c))
                pos_diags.add((r + c))
                neg_diags.add((r - c))
                dfs(r + 1)
                
                # backtrack
                board[r][c] = '.'
                cols.remove((c))
                pos_diags.remove((r + c))
                neg_diags.remove((r - c))
        
        dfs(0)
        return res