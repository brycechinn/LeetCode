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
    
    int count = 0;
    
    public int goodNodes(TreeNode root) {
        // approach: DFS while keeping track of max
        helper(root, Double.NEGATIVE_INFINITY);
        return count;
    }
    
    private void helper(TreeNode node, double max) {
        if (node == null) {
            return;
        }
        
        if (node.val >= max) {
            System.out.println(node.val + " >= " + max);
            count++;
        }
        
        max = Math.max(max, node.val);
        
        helper(node.left, max);
        helper(node.right, max);
    }
}