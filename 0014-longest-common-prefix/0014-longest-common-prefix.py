class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        i = 0
        while True:
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
            
            i += 1
            
        return ''