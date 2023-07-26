class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # approach 1: top-down DP, memoization of (i, j) : min operations
        '''
        dp = {}
        
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = 1 + min(dfs(i, j + 1),     # insert
                                     dfs(i + 1, j),     # delete
                                     dfs(i + 1, j + 1)) # replace
            return dp[(i, j)]

        return dfs(0, 0)
        '''
        # approach 2: bottom-up DP, tabulation where dp[i][j] = min operations
        # to convert word1[i:] to word2[j:]
        
        m, n = len(word1) + 1, len(word2) + 1
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        for r in range(m):
            dp[r][n - 1] = m - 1 - r
        
        for c in range(n):
            dp[m - 1][c] = n - 1 - c
        
        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(dp[r][c + 1],     # insert
                                       dp[r + 1][c],     # delete
                                       dp[r + 1][c + 1]) # replace

        return dp[0][0]
        
    def display(self, grid):
        for r in range(len(grid)):
            print(grid[r])
        