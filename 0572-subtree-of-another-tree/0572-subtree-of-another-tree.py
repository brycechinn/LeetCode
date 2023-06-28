# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # approach: top-down DFS, if roots match, call same tree
        
        isSameTree = True
        result = False
        
        def helper(p, q):
            nonlocal isSameTree
            nonlocal result
            
            if not p or not q:
                return
            
            if p.val == q.val:
                isSameTree = True
                sameTree(p, q)
                
                if isSameTree:
                    result = True
            
            helper(p.left, q)
            helper(p.right, q)
        
        def sameTree(p, q):
            nonlocal isSameTree
            
            if not p and not q:
                return
            
            if not p or not q:
                isSameTree = False
                return

            if p.val != q.val:
                isSameTree = False
            
            sameTree(p.left, q.left)
            sameTree(p.right, q.right)
        
        helper(root, subRoot)
        return result
        