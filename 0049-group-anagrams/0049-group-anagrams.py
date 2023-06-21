class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for s in strs:
            counts = [0] * 26
            
            for c in s:
                counts[ord(c) - ord('a')] += 1

            key = ' '.join([str(x) for x in counts])
            
            if key not in hashmap:
                hashmap[key] = []
            
            hashmap[key].append(s)
        
        return hashmap.values()