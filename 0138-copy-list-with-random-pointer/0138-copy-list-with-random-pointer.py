"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # approach: hashmap of old node : new node, two passes
        # 1st pass: add nodes to hashmap
        # 2nd pass: connect ptrs
        
        hashmap = { None : None }
        
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            hashmap[curr].next = hashmap[curr.next]
            hashmap[curr].random = hashmap[curr.random]
            curr = curr.next
            
        return hashmap[head]