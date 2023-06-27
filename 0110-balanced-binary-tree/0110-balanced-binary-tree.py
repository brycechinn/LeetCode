# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # approach: bottom-up DFS, compare left and right heights
        
        result = True
        
        def helper(node):
            nonlocal result
            
            if not node:
                return 0
            
            left = 1 + helper(node.left)
            right = 1 + helper(node.right)
            
            if abs(left - right) > 1:
                result = False
                
            return max(left, right)
        
        helper(root)
        return result