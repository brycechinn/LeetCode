class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # approach: maxheap of char counts, queue of (count, time + n)
        
        counts = Counter(tasks)
        heap = [-v for v in counts.values()]
        heapq.heapify(heap)
        
        queue = deque()
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
        