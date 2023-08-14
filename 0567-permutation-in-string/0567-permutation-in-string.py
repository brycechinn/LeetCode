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
            right_char = s2[r]
            d2[ord(right_char) - ord('a')] += 1
            
            if (not d1[ord(right_char) - ord('a')] or 
                d2[ord(right_char) - ord('a')] > d1[ord(right_char) - ord('a')]):
                while d1[ord(right_char) - ord('a')] != d2[ord(right_char) - ord('a')] and l <= r:
                    left_char = s2[l]
                    d2[ord(left_char) - ord('a')] -= 1
                    l += 1
            
            if d1 == d2:
                return True
        
        return False