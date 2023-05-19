class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        # approach 1: brute force, nested loop
        
        '''
        res = []
        
        for i, temp in enumerate(temperatures):
            j = i
            while j < len(temperatures) and temperatures[j] <= temp:
                j += 1
            
            if j == len(temperatures): # no warmer temperature
                res.append(0)
            else:
                res.append(j - i)
        
        return res
        '''
        
        # approach 2: monotonic decreasing stack
        
        res, stack = [0] * len(temperatures), []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                top = stack.pop()
                res[top] = i - top

            stack.append(i)
        return res
                
                    
            
        