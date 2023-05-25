class TimeMap:

    def __init__(self):
        self.hashmap = {} # key: list of (val, timestamp)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        
        self.hashmap[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        pairs = self.hashmap.get(key, [])
        res = ''
        
        l, r = 0, len(pairs) - 1
        while l <= r:
            m = (l + r) // 2
            
            if pairs[m][1] <= timestamp:
                res = pairs[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
                
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)