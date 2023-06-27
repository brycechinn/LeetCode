# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # approach: top-down DFS, get max of left and right heights
        
        def helper(node, height):
            if not node:
                return height
            
            left = helper(node.left, height + 1)
            right = helper(node.right, height + 1)
            
            return max(left, right)
        
        return helper(root, 0)
            
            