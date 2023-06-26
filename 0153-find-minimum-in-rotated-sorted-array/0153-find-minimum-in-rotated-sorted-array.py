class Solution:
    def findMin(self, nums: List[int]) -> int:
        # approach: binary search while checking for new min
        
        result = float('inf')
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            result = min(result, nums[m])
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
                
        return result