class TimeMap:

    def __init__(self):
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.d[key]
        result = ''
        
        # binary search
        l = 0
        r = len(pairs) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            value, current = pairs[m][0], pairs[m][1]
            
            if current == timestamp:
                return value

            if current > timestamp:
                r = m - 1
            else:
                l = m + 1
                result = value
        
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)