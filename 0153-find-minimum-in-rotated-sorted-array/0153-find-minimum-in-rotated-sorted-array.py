class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # approach: binary search to find inflection point,
        # i.e. nums[i] < nums[i - 1]
        
        l, r = 0, len(nums) - 1
        res = float(inf)
        
        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            
            if nums[m] < nums[r]:
                r = m - 1
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                break
            
        return res