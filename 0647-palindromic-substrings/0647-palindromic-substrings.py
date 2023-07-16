class Solution:
    def countSubstrings(self, s: str) -> int:
        # approach: longest palindromic substring except increment count
        # when a new palindrome is found
        
        count = 0
        
        for i in range(len(s)):
            # even length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            # odd length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
                
        return count