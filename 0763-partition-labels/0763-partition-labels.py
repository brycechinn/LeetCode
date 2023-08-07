class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        counts, window = {}, {}
        
        for c in s:
            counts[c] = 1 + counts.get(c, 0)
        
        length, matches, zeroes = 0, 0, len(counts)
        for c in s:
            if c not in window:
                zeroes -= 1
            
            window[c] = 1 + window.get(c, 0)
            length += 1
            
            if window[c] == counts[c]:
                matches += 1
            
            if matches + zeroes == len(counts):
                res.append(length)
                length, matches, zeroes = 0, 0, len(counts)
                window = {}
            
        return res