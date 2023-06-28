# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # approach: inorder traversal -> list
        
        nums = []
        
        def helper(node):
            if not node:
                return
            
            helper(node.left)
            nums.append(node.val)
            helper(node.right)
            
        helper(root)
        return nums[k - 1]