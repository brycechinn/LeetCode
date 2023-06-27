# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # approach: bottom-up DFS, get max of result and left height + right height
        
        result = -1
        
        def helper(node):
            nonlocal result
            
            if not node:
                return -1
            
            left = 1 + helper(node.left)
            right = 1 + helper(node.right)
            result = max(result, left + right)
            
            return max(left, right)
        
        helper(root)
        return result