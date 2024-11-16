class ListNode:
    '''
    A single node of a linked list.
    '''
    
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None

class LinkedList:
    '''
    A linked list with a dummy node. Each node value is unique.
    '''
    
    def __init__(self):
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

class TreeNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
        
    def add(self, val: int) -> None:
        '''
        Inserts a node with the given value into the BST. If it is already present, the
        BST is not modified.
        '''
        
        def helper(root, val):
            if not root:
                return TreeNode(val)

            if val < root.val:
                root.left = helper(root.left, val)
            elif val > root.val:
                root.right = helper(root.right, val)
            else:
                # node already in tree, so just return root
                pass
            
            return root
        
        self.root = helper(self.root, val)
        
    def remove(self, val: int) -> None:
        '''
        Removes a node with the given value from the BST. If it is not present,
        the BST is not modified.
        '''
        
        def findMin(root):
            if not root.left:
                return root.val
            
            return findMin(root.left)
        
        def helper(root, val):
            if not root:
                return None
            
            if val == root.val:
                if not root.left:
                    return root.right
                
                if not root.right:
                    return root.left
                
                # set root.val to min of right subtree
                root.val = findMin(root.right)
                
                # delete min of right subtree from right subtree
                root.right = helper(root.right, root.val)
            
            if val < root.val:
                root.left = helper(root.left, val)
            else:
                root.right = helper(root.right, val)
                
            return root
        
        self.root = helper(self.root, val)
    
    def contains(self, val) -> bool:
        '''
        Returns True if a node with the specified value exists in the
        BST, and False otherwise.
        '''
        
        def helper(root, val):
            if not root or val == root.val:
                return root
            
            return helper(root.left, val) if val < root.val else helper(root.right, val)
        
        return helper(self.root, val) is not None
    
class MyHashSet:
    # approach: array of buckets, each implemented as BST
    # time: O(1) amortized, space: O(n)
    
    def __init__(self):
        self.size = 997 # largest prime in [1, 1000]
        self.buckets = [BST() for i in range(self.size)]

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