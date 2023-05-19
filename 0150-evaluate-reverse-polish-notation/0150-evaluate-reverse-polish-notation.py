class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        # approach: push nums onto a stack, when an operand is found,
        # pop the stack twice and do the operation. then push the result
        # back onto the stack and continue
        
        if len(tokens) == 1: return int(tokens[0])
        
        operands = set(['+', '-', '*', '/'])
        stack, res = [], 0
        
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                
                print(left, right)
                
                if token == '+':
                    res = left + right
                elif token == '-':
                    res = left - right
                elif token == '*':
                    res = left * right
                else:
                    res = int(float(left) / float(right))
                
                stack.append(res)
        return res
        
        