class Solution:
    def longestPalindrome(self, s: str) -> str:
        # approach 1: generate every substring and check if each is palindrome
        
        longest = ''
        longest_length = 0
        palindromes = set()
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest_length:
                    longest = s[l:r + 1]
                    longest_length = r - l + 1
                
                l -= 1
                r += 1
                
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest_length:
                    longest = s[l:r + 1]
                    longest_length = r - l + 1
                
                l -= 1
                r += 1
            
        return longest