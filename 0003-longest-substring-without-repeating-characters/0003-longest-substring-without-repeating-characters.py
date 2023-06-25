class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # approach: sliding window, set of chars in current window
        
        if not s:
            return 0
        
        result = 0
        window = set()
        
        l = 0
        for r, c in enumerate(s):
            while c in window:
                window.remove(s[l])
                l += 1
            
            window.add(c)
            result = max(result, len(window))
        
        return result
            