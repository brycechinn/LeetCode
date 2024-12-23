# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # approach 1: binary search via recursion with helper function
        # time: O(H), space: O(H)
        # H = tree height
        '''
        if not root:
            return TreeNode(val)
        
        def helper(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            if not node:
                return
            
            if not node.left and val < node.val:
                node.left = TreeNode(val)
                return
            
            if not node.right and val > node.val:
                node.right = TreeNode(val)
                return
                    
            if val < node.val:
                helper(node.left, val)
            else:
                helper(node.right, val)
                    
        helper(root, val)
        return root
        '''
        
        # approach 2: binary search via recursion without helper function
        # time: O(H), space: O(H)
        # H = tree height
        
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        return root