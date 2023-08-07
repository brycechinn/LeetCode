class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        counts, window = {}, {}
        
        for c in s:
            counts[c] = 1 + counts.get(c, 0)
        
        length = 0
        for c in s:
            length += 1
            window[c] = 1 + window.get(c, 0)
            
            matches = 0
            for k in counts:
                if (k in window and window[k] == counts[k] or 
                    k not in window):
                    matches += 1
            
            if matches == len(counts):
                res.append(length)
                length = 0
                window = {}
            
        return res