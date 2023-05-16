class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # approach: sliding window with two dicts, compare have and need
        # instead of comparing entire dicts
        
        if len(s) < len(t): 
            return ''
        
        td, sd = {}, {}
        res = ''
        init = False
        
        for char in t:
            td[char] = 1 + td.get(char, 0)
        
        have, need = 0, len(td)
        
        l = 0
        for r, char in enumerate(s):
            sd[char] = 1 + sd.get(char, 0)
                
            if char in td and sd[char] == td[char]:
                have += 1
            
            while have == need:
                if not init:
                    res = s[l : r + 1]
                    init = True
                    
                if len(s[l : r + 1]) < len(res):
                    res = s[l : r + 1]
                
                sd[s[l]] -= 1
                    
                if s[l] in td and sd[s[l]] < td[s[l]]:
                    have -= 1
                    
                l += 1
        return res
        
        
        