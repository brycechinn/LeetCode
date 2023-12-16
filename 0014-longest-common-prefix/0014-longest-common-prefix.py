class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        i = 0
        while True:
            if i >= len(strs[0]):
                break
            
            c = strs[0][i]
            match = True
            
            for s in strs:
                if i >= len(s) or s[i] != c:
                    match = False
                    break
            
            if not match:
                break
            
            i += 1
            
        return strs[0][:i]