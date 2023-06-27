class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # approach: custom doubly-linked list, hashmap of key : node,
    # dummy left and right nodes

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = {}
        
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.delete(node)
        self.insert(node)
        
        return self.hashmap[key].val

    def insert(self, node: Node) -> None:
        temp = self.right.prev
        self.right.prev = node
        temp.next = node
        node.prev = temp
        node.next = self.right
        
    def delete(self, node: Node) -> None:
        next, prev = node.next, node.prev
        prev.next = next
        next.prev = prev
    
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.delete(self.hashmap[key])
            self.size -= 1
            
        node = Node(key, value)
        self.hashmap[key] = node
        self.insert(node)
        self.size += 1

        if self.size > self.capacity:
            lru = self.left.next
            lru.next.prev = self.left
            self.left.next = lru.next
            self.size -= 1
            del self.hashmap[lru.key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)