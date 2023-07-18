class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # approach: bottom-up DP, tabulation where dp[i][j] = ways to reach
        # target from point (i, j)
        
        # recurrence relation: dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        
        dp = [[0] * n for _ in range(m)]

        for r in range(m):
            dp[r][n - 1] = 1
        
        for c in range(n):
            dp[m - 1][c] = 1

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        
        return dp[0][0]
    
    def display(self, grid):
        for r in range(len(grid)):
            print(grid[r])