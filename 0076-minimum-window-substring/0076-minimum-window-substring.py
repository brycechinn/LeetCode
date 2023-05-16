class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if len(s) < len(t): 
            return ''
        
        td, sd = {}, {}
        res = ''
        init = False
        
        for char in t:
            td[char] = 1 + td.get(char, 0)
            sd[char] = 0
        
        have, need = 0, len(td)
        
        l = 0
        for r, char in enumerate(s):
            if char in sd:
                sd[char] += 1
                
                if sd[char] == td[char]:
                    have += 1
            
            while have == need:
                if not init:
                    res = (s[l : r + 1])
                    init = True
                    
                if len(s[l : r + 1]) < len(res):
                    res = (s[l : r + 1])
                
                if s[l] in sd:
                    sd[s[l]] -= 1
                    
                    if sd[s[l]] < td[s[l]]:
                        have -= 1
                    l += 1
                
                while l < r and s[l] not in sd:
                    l += 1
        return res
        
        
        