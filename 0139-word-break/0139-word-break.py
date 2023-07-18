class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # approach: bottom-up DP via iteration, tabulation of 
        # i : can remaining string be broken?
        
        # recurrence relation: dp[i] = dp[i + len(w)] for w in wordDict

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                    
                if dp[i]:
                    break

        return dp[0]