class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2): return False
        
        d1 = dict.fromkeys(string.ascii_lowercase, 0)
        d2 = dict.fromkeys(string.ascii_lowercase, 0)
        
        for char in s1:
            d1[char] += 1
        
        l = 0
        for r in range(len(s2)):
            char = s2[r]
            
            d2[char] += 1
                
            while d2[char] > d1[char]:
                d2[s2[l]] -= 1
                l += 1
            
            if d1 == d2:
                return True
            
        return False
    
        