class Solution:
    def longestPalindrome(self, s: str) -> str:
        # approach: iterate through s while expanding around center char, while loops
        # for odd and even length
        
        start, end = 0, 0
        longest = 0
        palindromes = set()
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    start, end = l, r
                    longest = r - l + 1
                
                l -= 1
                r += 1
                
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    start, end = l, r
                    longest = r - l + 1
                
                l -= 1
                r += 1
            
        return s[start:end + 1]