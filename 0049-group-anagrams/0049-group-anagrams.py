class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        
        for s in strs:
            counts = [0] * 26
            
            for c in s:
                counts[ord(c) - ord('a')] += 1
            
            key = tuple(counts)
            hashmap[key].append(s)
        
        return hashmap.values()