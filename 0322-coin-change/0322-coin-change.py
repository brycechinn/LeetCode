class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # approach: bottom-up DP, tabulation i : minimum num of coins that sum to i
        # recurrence relation: dp[i] = min(dp[i], 1 + dp[i - c]) for each coin c in coins
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for c in coins:
            if c <= amount:
                dp[c] = 1
        
        for i in range(1, amount + 1):
            for c in coins:
                if c > i:
                    continue
                    
                # recurrence relation
                dp[i] = min(dp[i], 1 + dp[i - c])

        return dp[amount] if dp[amount] != float('inf') else -1