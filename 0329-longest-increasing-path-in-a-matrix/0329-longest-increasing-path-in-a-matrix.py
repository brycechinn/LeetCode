class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # approach: top-down DP with memoization where dp[i][j] = longest increasing
        # path from matrix[i][j]
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(r, c, prev):
            if (r not in range(m) or 
                c not in range(n) or
                matrix[r][c] <= prev):
                return 0
            
            if dp[r][c]:
                return dp[r][c]

            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            longest = 0
            for dr, dc in directions:
                length = 1 + dfs(r + dr, c + dc, matrix[r][c])
                longest = max(longest, length)

            dp[r][c] = longest
            return dp[r][c]
        
        for r in range(m):
            for c in range(n):
                dfs(r, c, -1)

        return max([max(r) for r in dp])
    
    def display(self, grid):
        for r in range(len(grid)):
            print(grid[r])
            