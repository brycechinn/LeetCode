# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # approach: DFS, keep track of max
        
        def dfs(node, maximum):
            if not node:
                return 0
            
            if node.val < maximum:
                return dfs(node.left, maximum) + dfs(node.right, maximum)
            
            maximum = max(maximum, node.val)
            return 1 + dfs(node.left, maximum) + dfs(node.right, maximum)
        
        return dfs(root, float('-inf'))