class Solution:
    def longestPalindrome(self, s: str) -> str:
        # approach: iterate through s while expanding around center char, while loops
        # for odd and even length
        
        longest, start, end = 0, 0, 0

        def expand(l, r):
            nonlocal longest, start, end
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    start, end = l, r
                    longest = r - l + 1
                
                l -= 1
                r += 1
        
        for i in range(len(s)):
            expand(i, i)     # odd length
            expand(i, i + 1) # even length
        
        return s[start:end + 1]