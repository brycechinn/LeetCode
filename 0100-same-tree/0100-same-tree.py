# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # approach: top-down DFS, compare node values
        
        result = True
        
        def helper(p, q):
            nonlocal result
            
            if not p and not q:
                return
            
            if not p or not q:
                result = False
                return
            
            if p.val != q.val:
                result = False
            
            helper(p.left, q.left)
            helper(p.right, q.right)
        
        helper(p, q)
        return result
            