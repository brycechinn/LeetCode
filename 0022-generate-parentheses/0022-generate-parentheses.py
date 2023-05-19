class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        # approach: recursion
        
        if n == 1: 
            return ['()']
        
        res = []
        
        def generate(curr, opening, closing):
            if opening == 0 and closing == 0:
                res.append(curr)
            elif opening == closing:
                generate(curr + '(', opening - 1, closing)
            elif opening > 0 and closing > 0:
                generate(curr + '(', opening - 1, closing)
                generate(curr + ')', opening, closing - 1)
            else:
                generate(curr + ')', opening, closing - 1)
        
        curr = '('
        opening, closing = n - 1, n
        generate(curr, opening, closing)
        
        return res
        