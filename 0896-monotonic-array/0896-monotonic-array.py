class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # approach: linear scan to check increasing or decreasing
        # time: O(n), space: O(1)
        
        increasing, decreasing = True, True 
        inc_prev, dec_prev = float('-inf'), float('inf')
        
        for num in nums:
            if num < inc_prev:
                increasing = False
            
            if num > dec_prev:
                decreasing = False
            
            inc_prev = num
            dec_prev = num
        
        return increasing or decreasing