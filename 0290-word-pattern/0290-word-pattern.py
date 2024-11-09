class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # approach: mapping of char: str
        # time: O(n), space: O(n)
        
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        c_to_w, w_to_c = {}, {}
        
        for i, c in enumerate(pattern):
            w = words[i]
            
            if (c in c_to_w and c_to_w[c] != w or
                w in w_to_c and w_to_c[w] != c):
                return False
            
            if c in c_to_w or w in w_to_c:
                continue
                
            c_to_w[c] = w
            w_to_c[w] = c
        
        return True