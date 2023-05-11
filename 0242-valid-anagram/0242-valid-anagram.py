class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # approach: one dict for each string, then compare dicts
        
        if s == t:
            return True
        
        if len(s) != len(t):
            return False
        
        sd = dict()
        td = dict()
        
        for char in s:
            if char in sd:
                sd[char] += 1
            else:
                sd[char] = 1
        
        for char in t:
            if char in td:
                td[char] += 1
            else:
                td[char] = 1
        
        return sd == td