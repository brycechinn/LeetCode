class TimeMap:

    def __init__(self):
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.d[key]
        result = ('', 0)
        
        # binary search
        l = 0
        r = len(pairs) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            current = pairs[m][1]
            
            if current == timestamp:
                return pairs[m][0]

            if current > timestamp:
                r = m - 1
            else:
                l = m + 1
                
                # potential new result
                if current > result[1]:
                    result = pairs[m]
        
        return result[0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)