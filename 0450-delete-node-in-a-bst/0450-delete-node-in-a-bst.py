# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # approach: search for node, and if found, set parent equal to left
        # (or right?) child of node to delete
        
        if not root:
            return None
        
        if key == root.val:
            if not root.left and not root.right:
                # node to delete is leaf node
                return None
            
            if root.left:
                temp = root.right
                root = root.left
                root.right = self.insert(root.right, temp) if temp else root.right
                return root
            else:
                temp = root.left
                root = root.right
                root.left = self.insert(root.left, temp) if temp else root.left
                return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root
    
    def insert(self, root, node):
        if not root:
            return node
    
        if node.val < root.val:
            root.left = self.insert(root.left, node)
        else:
            root.right = self.insert(root.right, node)
            
        return root