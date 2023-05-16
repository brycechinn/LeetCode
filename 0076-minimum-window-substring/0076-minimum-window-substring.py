class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        def isValidWindow(sd, td):
            for char in td:
                if sd[char] < td[char]:
                    return False
            
            return True
        
        if len(s) < len(t): 
            return ''
        
        td = {}
        sd = {}
        res = ''
        init = False
        
        for char in t:
            td[char] = 1 + td.get(char, 0)
            sd[char] = 0
            
        print(td, sd)
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            
            if char in td:
                sd[char] += 1
            
            while isValidWindow(sd, td):
                if not init:
                    res = (s[l : r + 1])
                    init = True
                    
                if len(s[l : r + 1]) < len(res):
                    res = (s[l : r + 1])
                    
                if s[l] in sd:
                    sd[s[l]] -= 1
                    
                l += 1
                
                while l < r and s[l] not in td:
                    l += 1
        return res
        
        
        