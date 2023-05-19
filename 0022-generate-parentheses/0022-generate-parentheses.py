class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        # approach: stack + backtracking
        
        stack, res = [], []
        
        def backtrack(opening, closing):
            if opening == closing == n:
                res.append(''.join(stack))
                return
            
            if opening < n:
                stack.append('(')
                backtrack(opening + 1, closing)
                stack.pop() # backtrack
            
            if closing < opening:
                stack.append(')')
                backtrack(opening, closing + 1)
                stack.pop() # backtrack
        
        backtrack(0, 0)
        return res
        
        '''
        if n == 1: 
            return ['()']
        
        res = []
        
        def generate(curr, opening, closing):
            if opening == 0 and closing == 0:
                res.append(curr)
            elif opening == closing:
                generate(curr + '(', opening - 1, closing)
            elif opening == 0:
                generate(curr + ')', opening, closing - 1)
            else:
                generate(curr + '(', opening - 1, closing)
                generate(curr + ')', opening, closing - 1)
        
        curr = '('
        opening, closing = n - 1, n
        generate(curr, opening, closing)
        
        return res
        '''
        