class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # approach: binary search
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (r + l) // 2
            print(m)
            
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return -1