class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # approach: backtracking with stack.pop()
        
        result = []
        stack = []
        
        def helper(opening, closing):
            if closing == n:
                combo = ''
                
                for p in stack:
                    combo += p
                
                result.append(combo)
                return
            
            if opening < n:
                stack.append('(')
                helper(opening + 1, closing)
                stack.pop()
            
            if closing < opening:
                stack.append(')')
                helper(opening, closing + 1)
                stack.pop()
        
        helper(0, 0)
        return result
        