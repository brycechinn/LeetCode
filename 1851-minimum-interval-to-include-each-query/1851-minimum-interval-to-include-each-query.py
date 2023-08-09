class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # approach: for each query, two phases: add potential intervals to minheap,
        # pop invalid intervals from minheap
        
        intervals.sort()
        res, heap, i = {}, [], 0
        
        for q in sorted(queries):
            
            # add intervals to minheap
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            
            # pop from minheap
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            res[q] = heap[0][0] if heap else -1
        
        return [res[q] for q in queries]