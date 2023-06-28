# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # approach: DFS, keep track of min and max, must be within range
        
        res = True
        
        def helper(node, minimum, maximum):
            nonlocal res
            
            if not node:
                return
            
            if node.val <= minimum or node.val >= maximum:
                res = False
            
            helper(node.left, minimum, min(maximum, node.val))
            helper(node.right, max(minimum, node.val), maximum)
            
        helper(root, float('-inf'), float('inf'))
        return res
            