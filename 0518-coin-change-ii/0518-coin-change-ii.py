class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # approach 1: backtracking DFS (TLE)
        '''
        res = 0
        
        def dfs(i, total):
            nonlocal res
            
            if total == amount:
                res += 1
                return
            
            if i == len(coins) or total > amount:
                return
            
            # include num, don't increment i
            dfs(i, total + coins[i])
            
            # don't include num, increment i
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res
        '''
        # approach 2: memoization
        '''
        dp = {}
        
        def dfs(i, remaining):
            if (i, remaining) in dp:
                return dp[(i, remaining)]
            
            if remaining == 0:
                return 1
            
            if i == len(coins) or remaining < 0:
                return 0

            dp[(i, remaining)] = (dfs(i, remaining - coins[i]) + 
                                  dfs(i + 1, remaining))
            
            return dp[(i, remaining)]
            
        return dfs(0, amount)
        '''
        # approach 3: bottom-up DP
        
        m, n = amount + 1, len(coins)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for c in range(n):
            dp[m - 1][c] = 1 
        
        for r in range(m - 2, -1, -1):
            for c in range(n - 1, -1, -1):
                down = dp[r + coins[c]][c] if r + coins[c] in range(m) else 0
                right = dp[r][c + 1] if c + 1 in range(n) else 0
                dp[r][c] = down + right
   
        return dp[0][0]
        
    def display(self, board):
        for row in board:
            print(row)