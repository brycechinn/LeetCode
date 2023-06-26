class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # approach: binary search while keeping track of left and right
        # sorted portions
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if nums[m] >= nums[l]: # left sorted portion
                if target < nums[m] and target >= nums[l]:
                    # search left
                    r = m - 1
                else:
                    # search right
                    l = m + 1
            else: # right sorted portion
                if target > nums[m] and target <= nums[r]:
                    # search right
                    l = m + 1
                else:
                    # search left
                    r = m - 1
        return -1