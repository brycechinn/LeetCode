class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # approach: sliding window, two hashmaps of char : frequency
        
        if len(s1) > len(s2):
            return False
        
        d1, d2 = [0] * 26, [0] * 26
        
        for c in s1:
            d1[ord(c) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            index = ord(s2[r]) - ord('a')
            d2[index] += 1
            
            if d1[index] == 0 or d2[index] > d1[index]:
                while d1[index] != d2[index] and l <= r:
                    d2[ord(s2[l]) - ord('a')] -= 1
                    l += 1
            
            if d1 == d2:
                return True
        
        return False