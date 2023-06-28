# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # approach: 3 cases
        # if p and q < root, go left
        # if p and q > root, go right
        # else return root

        def helper(node):
            nonlocal p
            nonlocal q
            
            if p.val < node.val and q.val < node.val:
                return helper(node.left)
            
            if p.val > node.val and q.val > node.val:
                return helper(node.right)
            
            return node
        
        return helper(root)
                