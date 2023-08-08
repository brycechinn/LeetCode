class Solution:
    def checkValidString(self, s: str) -> bool:
        # approach: greedy, keep track of leftMin and leftMax
        
        left_min, left_max = 0, 0
        for p in s:
            if p == '(':
                left_min += 1
                left_max += 1
            elif p == ')':
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1
            
            left_min = max(0, left_min)
            
            if left_max < 0:
                return False
        
        return left_min == 0
        
        