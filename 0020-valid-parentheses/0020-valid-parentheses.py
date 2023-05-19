class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) == 1:
            return False
        
        d = { '(' : ')', '{' : '}', '[' : ']' }
        stack = []
        
        for char in s:
            # opening brace
            if char in d:
                stack.append(char)
            # closing brace
            else:
                # if not empty and char matches top brace
                if stack and char == d[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return not stack