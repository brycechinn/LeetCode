class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # approach: stack
        
        if len(tokens) == 1:
            return int(tokens[0])
        
        ops = {'+', '-', '*', '/'}
        stack = []
        
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                right, left = stack.pop(), stack.pop()
                
                if t == '+':
                    stack.append(left + right)
                elif t == '-':
                    stack.append(left - right)
                elif t == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
                    
        return stack[0]