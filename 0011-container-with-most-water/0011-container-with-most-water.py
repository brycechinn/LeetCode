class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        
        return res
                