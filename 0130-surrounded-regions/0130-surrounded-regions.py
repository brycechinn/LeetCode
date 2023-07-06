class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # approach: call DFS from all edges, then flip nodes that
        # haven't been marked as visited
        
        m, n = len(board), len(board[0])
        
        def dfs(r, c):
            if (r not in range(m) or 
                c not in range(n) or 
                board[r][c] != 'O'):
                return
            
            board[r][c] = 'T'
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)
        
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                
                if board[r][c] == 'T':
                    board[r][c] = 'O'