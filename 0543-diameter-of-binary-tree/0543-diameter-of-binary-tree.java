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
        // approach: get left height + right height at each node, bottom up
        
        helper(root);
        return result;
    }
    
    private int helper(TreeNode node) {
        if (node == null) {
            return -1;
        }
        
        int maxL = 1 + helper(node.left);
        int maxR = 1 + helper(node.right);
        result = Math.max(result, maxL + maxR);
        
        return Math.max(maxL, maxR);
    }
}