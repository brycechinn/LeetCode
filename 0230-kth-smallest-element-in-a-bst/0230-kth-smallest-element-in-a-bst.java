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
    
    List<Integer> list = new ArrayList<>();
    
    public int kthSmallest(TreeNode root, int k) {
        // approach: in-order traversal -> array
        
        helper(root);
        
        return list.get(k - 1);
    }
    
    private void helper(TreeNode node) {
        if (node == null) {
            return;
        }
        
        helper(node.left);
        // in-order processing
        list.add(node.val);
        helper(node.right);
    }
}