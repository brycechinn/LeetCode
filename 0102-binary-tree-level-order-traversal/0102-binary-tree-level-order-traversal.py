# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # approach: queue
        
        if not root:
            return []
        
        q = collections.deque()
        q.append(root)
        res = []
        
        while q:
            level = []
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            res.append(level)
        
        return res
        