class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # approach 1: top-down DP via memoization with cache of 
        # (i, total) : unique combinations

        '''
        dp = {}
        
        def dfs(i, remaining):
            if i == len(coins) or remaining < 0:
                return 0
            
            if remaining == 0:
                return 1
            
            if (i, remaining) in dp:
                return dp[(i, remaining)]

            dp[(i, remaining)] = dfs(i, remaining - coins[i]) + dfs(i + 1, remaining)
            return dp[(i, remaining)]
        
        return dfs(0, amount)
        '''
        
        # approach 2: bottom-up DP via tabulation
        
        m, n = len(coins), amount + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for r in range(m):
            dp[r][n - 1] = 1
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 2, -1, -1):
                dp[r][c] = dp[r + 1][c] if r + 1 < m else 0
                
                if c + coins[r] < n:
                    dp[r][c] += dp[r][c + coins[r]]

        return dp[0][0]
        
    def display(self, grid):
        for r in range(len(grid)):
            print(grid[r])