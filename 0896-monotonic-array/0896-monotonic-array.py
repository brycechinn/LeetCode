class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # approach: two linear scans to check increasing and decreasing
        # time: O(n), space: O(1)
        
        increasing, prev = True, float('-inf')
        
        for num in nums:
            if num < prev:
                increasing = False
            
            prev = num
        
        decreasing, prev = True, float('inf')
        
        for num in nums:
            if num > prev:
                decreasing = False
                
            prev = num
        
        return increasing or decreasing