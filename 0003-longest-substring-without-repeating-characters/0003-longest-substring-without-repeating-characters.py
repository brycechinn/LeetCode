class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # approach: sliding window, set to store current window
        
        if not s:
            return 0
        
        l = 0
        window = set()
        longest = 0
        
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
                    
            window.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1

        return longest
    
    
        
    
    
                
        
        