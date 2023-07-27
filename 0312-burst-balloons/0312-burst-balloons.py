class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # approach 1: top-down DP, memoization of (l, r) : coins, pop ith balloon last

        nums = [1] + nums + [1]
        dp = {}
        
        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            max_coins = 0
            for i in range(l, r + 1):
                remaining = dfs(l, i - 1) + dfs(i + 1, r)
                gain = nums[l - 1] * nums[i] * nums[r + 1]
                max_coins = max(max_coins, remaining + gain)
            
            dp[(l, r)] = max_coins
            return max_coins
        
        return dfs(1, len(nums) - 2)