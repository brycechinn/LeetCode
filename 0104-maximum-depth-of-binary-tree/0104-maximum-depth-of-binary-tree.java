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
    public int maxDepth(TreeNode root) {
        // approach: recursive DFS
        
        return helper(root, 0);
    }
    
    private int helper(TreeNode node, int depth) {
        if (node == null) {
            return depth;
        }
        
        return Math.max(helper(node.left, depth + 1), helper(node.right, depth + 1));
    }
}