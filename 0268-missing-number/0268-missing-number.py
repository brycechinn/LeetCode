class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # approach 1: Gauss summation
        '''
        n = len(nums)
        total = (n * (n + 1)) // 2 # Gauss summation
        return total - sum(nums)
        '''
        
        # approach 2: XOR of nums, then XOR of [0, n]
        
        res = 0
        
        for n in nums:
            res = res ^ n
            
        for n in range(len(nums) + 1):
            res = res ^ n
        
        return res