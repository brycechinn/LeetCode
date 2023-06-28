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
        
        res = None
        
        def helper(node):
            nonlocal res
            nonlocal p
            nonlocal q
            
            if not node:
                return
            
            if p.val < node.val and q.val < node.val:
                helper(node.left)
            elif p.val > node.val and q.val > node.val:
                helper(node.right)
            else:
                res = node
        
        helper(root)
        return res
                