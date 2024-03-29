/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // approach: recursion, use inorder array to find "split" in remaining nodes
        
        if (preorder.length == 0 || inorder.length == 0) {
            return null;
        }
        
        TreeNode root = new TreeNode(preorder[0]);

        // find root index in inorder
        int mid = 0;
        for (int i = 0; i < inorder.length; i++) {
            if (inorder[i] == root.val) {
                mid = i;
            }
        }
        
        root.left = 
            buildTree(
                Arrays.copyOfRange(preorder, 1, mid + 1),
                Arrays.copyOfRange(inorder, 0, mid)
            );
        
        root.right = 
            buildTree(
                Arrays.copyOfRange(preorder, mid + 1, preorder.length),
                Arrays.copyOfRange(inorder, mid + 1, inorder.length)
            );
        
        return root;
    }
}