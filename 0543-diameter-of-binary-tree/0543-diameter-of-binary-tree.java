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
    
    int result = -1;
    
    public int diameterOfBinaryTree(TreeNode root) {
        helper(root);
        
        return result;
    }
    
    public int helper(TreeNode node) {
        if (node == null) {
            return -1;
        }
        
        int left = 1 + helper(node.left);
        int right = 1 + helper(node.right);
        
        result = Math.max(result, left + right);
        
        return Math.max(left, right);
    }
}