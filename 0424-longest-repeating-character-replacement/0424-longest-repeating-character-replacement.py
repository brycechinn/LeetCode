class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # approach: hashmap of char : frequency in current window
        # window size: r - l + 1

        d = collections.defaultdict(int)
        result = 0
        
        l = 0
        for r, c in enumerate(s):
            d[c] += 1
            count = max(d.values())
            
            while (r - l + 1) - count > k:
                d[s[l]] -= 1
                l += 1
                count = max(d.values())
            
            result = max(result, r - l + 1)
            
        return result
            