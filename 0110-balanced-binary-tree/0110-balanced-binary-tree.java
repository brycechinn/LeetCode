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
    
    boolean result = true;
    
    public boolean isBalanced(TreeNode root) {
        helper(root);
        return result;
    }
    
    private int helper(TreeNode node) {
        if (node == null) {
            return -1;
        }
        
        int heightL = 1 + helper(node.left);
        int heightR = 1 + helper(node.right);
        
        if (Math.abs(heightL - heightR) > 1) {
            result = false;
        }
        
        return Math.max(heightL, heightR);
    }
}