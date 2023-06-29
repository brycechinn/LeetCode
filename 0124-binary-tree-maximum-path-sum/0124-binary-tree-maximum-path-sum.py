# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # approach: DFS, pass max path sum WITHOUT split to parent
        # keep track of max path sum WITH split as global var
        
        res = float('-inf')
        
        def helper(node):
            nonlocal res
            
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            left = max(0, left)
            right = max(0, right)
        
            sum_without_split = node.val + max(left, right)
            sum_with_split = node.val + left + right
            
            res = max(res, sum_with_split)
            
            return sum_without_split
        
        helper(root)
        return res
            
            