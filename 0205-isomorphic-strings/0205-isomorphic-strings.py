class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd, td = {}, {}
        
        for i in range(len(s)):
            sc, tc = s[i], t[i]
            
            if ((sc in sd and sd[sc] != tc) or
                (tc in td and td[tc] != sc)):
                return False
            
            td[tc] = sc
            sd[sc] = tc
        
        return True