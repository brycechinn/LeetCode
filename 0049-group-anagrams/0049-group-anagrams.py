class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        def isAnagram(a, b):
            return sorted(a) == sorted(b)
        
        d = {}
        
        for s in strs:
            srt = str(sorted(s))
            
            if srt not in d:
                d[srt] = [s]
            else:
                d[srt].append(s)
        
        return d.values()
        