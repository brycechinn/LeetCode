class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # approach: top-down memoization via DFS and cache of
        # (i, holding) : max_profit
        
        dp = {}

        def dfs(i, holding):
            if i >= len(prices):
                return 0
            
            if (i, holding) in dp:
                return dp[(i, holding)]
            
            # cooldown
            c = dfs(i + 1, holding)
            if holding:
                # sell
                s = dfs(i + 2, False) + prices[i]
                max_profit = max(c, s)
            else:
                # buy
                b = dfs(i + 1, True) - prices[i]
                max_profit = max(c, b)
            
            dp[(i, holding)] = max_profit
            return max_profit
                
        return dfs(0, False)