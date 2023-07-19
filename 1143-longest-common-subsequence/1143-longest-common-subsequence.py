class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # approach: bottom-up DP with tabulation where dp[i][j] = LCS between
        # text1[i:] and text2[j:]
        
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]
    
    def display(self, grid):
        for r in range(len(grid)):
            print(grid[r])