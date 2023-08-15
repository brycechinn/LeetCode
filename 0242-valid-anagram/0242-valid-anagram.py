class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # approach: two arrays of char counts, compare
        
        if len(s) != len(t):
            return False
        
        s_counts, t_counts = [0] * 26, [0] * 26
        
        for i in range(len(s)):
            s_counts[ord(s[i]) - ord('a')] += 1
            t_counts[ord(t[i]) - ord('a')] += 1
        
        return s_counts == t_counts