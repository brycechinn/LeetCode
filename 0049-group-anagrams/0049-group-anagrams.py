class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # approach 1: categorize by sorted string
        
        '''
        d = {}
        
        for s in strs:
            srt = str(sorted(s))
            
            if srt not in d:
                d[srt] = [s]
            else:
                d[srt].append(s)
        
        return d.values()
        '''
        
        # approach 2: categorize by character count
        
        d = {}
        
        for s in strs:
            
            key = [0] * 26
            
            for c in s:
                index = ord(c) - ord('a')
                key[index] += 1
                
            key = tuple(key)
                
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        
        return d.values()