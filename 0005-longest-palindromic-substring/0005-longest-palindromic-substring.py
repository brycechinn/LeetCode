class Solution:
    def longestPalindrome(self, s: str) -> str:
        # approach: expand around center function
        
        longest, start, end = 0, 0, 0
        
        def expand(l, r):
            nonlocal longest, start, end

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > longest:
                    longest = r - l
                    start, end = l, r
                    
                l -= 1
                r += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
    
        return s[start:end + 1]