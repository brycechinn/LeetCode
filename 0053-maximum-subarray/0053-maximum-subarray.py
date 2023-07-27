class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # approach 1: compute sum of all subarrays (TLE)
        '''
        res = min(nums)
        
        for i in range(len(nums)):
            total = 0
            
            for j in range(i, len(nums)):
                total += nums[j]
                res = max(res, total)
        
        return res
        '''
        # approach 2: greedy, reset total when it becomes negative
        
        res, total = nums[0], 0
        
        for r in range(len(nums)):
            if total < 0:
                total = 0
            
            total += nums[r]
            res = max(res, total)
        
        return res
