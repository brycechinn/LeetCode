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
    
    public boolean isValidBST(TreeNode root) {
        // approach: DFS
        
        helper(root, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
        return result;
    }
    
    private void helper(TreeNode node, double lower, double upper) {
        if (node == null) {
            return;
        }
        
        if (node.val <= lower || node.val >= upper) {
            result = false;
        }
        
        helper(node.left, lower, Math.min(upper, node.val));
        helper(node.right, Math.max(lower, node.val), upper);
    }
}