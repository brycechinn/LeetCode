class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # approach: move pointer along x-axis while keeping track of "holes", i.e.
        # spaces from shorter bars. move pointer until bar of >= height is found,
        # then add the area of all of the holes. do the same thing with a right
        # pointer
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
            
                
                
            
            