class ListNode:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.next = None

class MyHashSet:
    # approach: array of linked lists
    # time: O(1) amortized, space: O(n)
    
    def __init__(self):
        self.size = 9999
        self.buckets = [ListNode() for i in range(self.size)]

    def add(self, key: int) -> None:
        i = self.hashFunc(key)
        prev = self.buckets[i]
        curr = prev.next
        
        while (curr):
            if curr.val == key:
                return
            
            prev = curr
            curr = curr.next

        prev.next = ListNode(key)

    def remove(self, key: int) -> None:
        i = self.hashFunc(key)
        prev = self.buckets[i]
        curr = prev.next
        
        while (curr):
            if curr.val == key:
                prev.next = curr.next
                return
            
            prev = curr
            curr = curr.next
                
    def contains(self, key: int) -> bool:
        i = self.hashFunc(key)
        prev = self.buckets[i]
        curr = prev.next
        
        while (curr):
            if curr.val == key:
                return True
        
            prev = curr
            curr = curr.next
        
        return False
            
    def hashFunc(self, key: int) -> int:
        return key % self.size
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)