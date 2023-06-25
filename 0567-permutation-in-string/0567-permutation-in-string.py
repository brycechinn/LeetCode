class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counts1 = [0] * 26
        counts2 = [0] * 26

        l = 0
        r = 0
        for i in range(len(s1)):
            c1 = s1[i]
            c2 = s2[i]
            
            counts1[ord(c1) - ord('a')] += 1
            counts2[ord(c2) - ord('a')] += 1
            r += 1
        
        if counts1 == counts2:
            return True
        
        r -= 1
        while r < len(s2) - 1:
            counts2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            counts2[ord(s2[r]) - ord('a')] += 1

            if counts1 == counts2:
                return True
        
        return False
            
            
            