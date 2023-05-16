class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        # approach: sliding window, two dicts to store char counts,
        # compare dicts at each iteration
        
        if len(s1) > len(s2): return False
        
        d1 = dict.fromkeys(string.ascii_lowercase, 0)
        d2 = dict.fromkeys(string.ascii_lowercase, 0)
        
        for char in s1:
            d1[char] += 1
        
        l = 0
        for r in range(len(s2)):
            rc = s2[r]
            d2[rc] += 1
                
            while d2[rc] > d1[rc]:
                lc = s2[l]
                d2[lc] -= 1
                l += 1
            
            if d1 == d2:
                return True
            
        return False
    
        