class ListNode:
    '''
    A single node of a linked list.
    '''
    
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.next = None

class LinkedList:
    '''
    A linked list with a dummy node. Each node value is unique.
    '''
    
    def __init__(self) -> None:
        self.head = ListNode()
        
    def add(self, val: int) -> None:
        '''
        Adds a node with the specified value to the end of the linked list.
        If it is already present, the linked list is not modified.
        '''
        
        prev = self.head
        curr = prev.next
        
        while curr:
            if curr.val == val:
                return
            
            prev = curr
            curr = curr.next

        prev.next = ListNode(val)
        
    def remove(self, val: int) -> None:
        '''
        Removes a node with the specified value from the linked list.
        If it is not present, the linked list is not modified.
        '''
    
        prev = self.head
        curr = prev.next
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                return
            
            prev = curr
            curr = curr.next
    
    def contains(self, val: int) -> bool:
        '''
        Returns True if a node with the specified value exists in the
        linked list, and False otherwise.
        '''
        
        prev = self.head
        curr = prev.next
        
        while curr:
            if curr.val == val:
                return True
        
            prev = curr
            curr = curr.next
        
        return False
    
class MyHashSet:
    # approach: array of buckets, each implemented as linked list
    # time: O(1) amortized, space: O(n)
    
    def __init__(self):
        self.size = 997 # largest prime in [1, 1000]
        self.buckets = [LinkedList() for i in range(self.size)]

    def add(self, key: int) -> None:
        bucket = self.buckets[self.hashFunc(key)]
        bucket.add(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self.hashFunc(key)]
        bucket.remove(key)
                
    def contains(self, key: int) -> bool:
        bucket = self.buckets[self.hashFunc(key)]
        return bucket.contains(key)
            
    def hashFunc(self, key: int) -> int:
        return key % self.size
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)