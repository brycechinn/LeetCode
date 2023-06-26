class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # approach: when encounter an operand, pop stack twice, do operation, push result
        
        ops = {'+', '-', '*', '/'}
        stack = []
        
        for t in tokens:
            if stack and t in ops:
                right = stack.pop()
                left = stack.pop()
                
                if t == '+':
                    stack.append(left + right)
                elif t == '-':
                    stack.append(left - right)
                elif t == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
            else:
                stack.append(int(t))
        
        return stack.pop()