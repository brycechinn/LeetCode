class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # approach: sliding window, two hashmaps of char : frequency
        
        if len(s1) > len(s2):
            return False
        
        d1, d2 = {}, {}
        
        for c in s1:
            d1[c] = 1 + d1.get(c, 0)

        l = 0
        for r in range(len(s2)):
            head = s2[r]
            d2[head] = 1 + d2.get(head, 0)
            
            if head not in d1 or d1[head] < d2[head]:
                while d1.get(head, 0) != d2.get(head, 0) and l <= r:
                    tail = s2[l]
                    d2[tail] -= 1
                    l += 1
            
            matches = 0
            for c in d1:
                if d1.get(c, 0) == d2.get(c, 0):
                    matches += 1
            
            if matches == len(d1):
                return True
        
        return False