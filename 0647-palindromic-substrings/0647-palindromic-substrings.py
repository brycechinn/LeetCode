class Solution:
    def countSubstrings(self, s: str) -> int:
        # approach: longest palindromic substring except increment count
        # when a new palindrome is found
        
        count = 0
        
        def expand(l, r):
            nonlocal count
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            expand(i, i)     # odd length
            expand(i, i + 1) # even length
                
        return count