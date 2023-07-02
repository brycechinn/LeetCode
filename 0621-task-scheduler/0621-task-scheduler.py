class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # approach: maxheap of char counts, queue of (count, time + n)
        
        counts = collections.Counter(tasks)
        heap = []
        
        for v in counts.values():
            heap.append(-1 * v)
        
        heapq.heapify(heap)
        queue = collections.deque()
        time = 0
        
        while heap or queue:
            
            if not heap and queue[0][1] > time:
                time += 1
                continue
            
            if queue and queue[0][1] <= time:
                heapq.heappush(heap, queue.popleft()[0])
    
            num = heapq.heappop(heap)
            time += 1
            
            if num + 1 < 0:
                queue.append((num + 1, time + n))
            
        return time
        