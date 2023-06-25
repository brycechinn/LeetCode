class Solution:
    def isValid(self, s: str) -> bool:
        d = { '(': ')', '{': '}', '[': ']' }
        stack = []
        
        for p in s:
            if p in d:
                stack.append(p)
            else:
                if stack and p == d[stack[-1]]:
                    stack.pop()
                else:
                    return False
            
            
            '''
            if stack:
                if p in d:
                    stack.append(p)
                else:
                    if p == d[stack[-1]]:
                        stack.pop()
                    else:
                        return False
            else:
                if p in d:
                    stack.append(p)
                else:
                    return False
            '''
        
        return not stack