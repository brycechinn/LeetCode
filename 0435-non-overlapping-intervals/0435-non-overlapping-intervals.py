class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # approach: sort intervals, then compare current start to
        # previous end
        
        intervals.sort()
        prev_end = intervals[0][1]
        res = 0
        
        for curr_start, curr_end in intervals[1:]:
            if curr_start >= prev_end:
                prev_end = curr_end
            else:
                res += 1
                prev_end = min(prev_end, curr_end)
        
        return res