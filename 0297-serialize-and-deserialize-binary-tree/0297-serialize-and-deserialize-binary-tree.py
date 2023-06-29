# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # approach: preorder traversal + '#' + inorder traversal

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        preorder = []
        
        def helper(node):
            nonlocal preorder
            
            if not node:
                preorder.append('N')
                return
            
            preorder.append(str(node.val))
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return ','.join(preorder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        preorder = data.split(',')
        i = 0

        def helper():
            nonlocal i
            
            if preorder[i] == 'N':
                i += 1
                return None
            
            node = TreeNode(int(preorder[i]))
            i += 1
            
            node.left = helper()
            node.right = helper()
            
            return node

        return helper()
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))