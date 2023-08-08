class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # approach: sort intervals then compare start of current
        # interval to end of previous interval
        
        intervals.sort(key=lambda x: x[0])
        
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            prev_end = res[-1][1]
            
            if start <= prev_end:
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start, end])
                
        return res