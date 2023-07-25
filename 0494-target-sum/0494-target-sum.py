class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # approach 1: DFS (TLE)
        
        dp = {}
 
        def dfs(i, total):
            if (i, total) in dp:
                return dp[(i, total)]
            
            if i == len(nums):
                if total == target:
                    return 1
                return 0

            dp[(i, total)] =  (dfs(i + 1, total - nums[i]) + 
                               dfs(i + 1, total + nums[i]))
            return dp[(i, total)]
        
        return dfs(0, 0)