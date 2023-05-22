class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
    
        # maintain stack of start index : height, pop when histogram is no longer
        # non-decreasing
        
        if len(heights) == 1:
            return heights[0]
    
        res = 0
        stack = []
        
        for i, height in enumerate(heights):
            start = i

            while stack and height < stack[-1][1]:
                start, h = stack.pop()
                res = max(res, (i - start) * h)

            stack.append((start, height))
                
        while stack:
            start, h = stack.pop()
            res = max(res, (len(heights) - start) * h)

        return res
        
        