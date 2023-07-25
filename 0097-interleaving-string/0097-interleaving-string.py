class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # approach 1: top-down DP, memoization of (i, j) : isInterleaving
        '''
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = {}
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i == len(s1) and j == len(s2):
                return True
            
            if (i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j) or 
                j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1)):
                return True

            dp[(i, j)] = False
            return False
        
        return dfs(0, 0)
        '''
        # approach 2: bottom-up DP where dp[i][j] = s3 is an interleaving of 
        # s1[i:] and s2[j:]
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        m, n = len(s1), len(s2)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[m][n] = True
        
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if (i < m and s1[i] == s3[i + j] and dp[i + 1][j] or 
                    j < n and s2[j] == s3[i + j] and dp[i][j + 1]):
                    dp[i][j] = True
        
        # self.display(dp)
        
        return dp[0][0]
        
    def display(self, grid):
        for r in range(len(grid)):
            print(grid[r])