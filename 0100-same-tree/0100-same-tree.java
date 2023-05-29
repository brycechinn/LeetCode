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
    
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // approach: do DFS on both trees at the same time
        
        dfs(p, q);
        return result;
    }
    
    public void dfs(TreeNode p, TreeNode q) {
        if (p == null || q == null) {
            if (!(p == null && q == null)) {
                result = false;
            }
            
            return;
        }
        
        dfs(p.left, q.left);
        dfs(p.right, q.right);
        
        if (p.val != q.val) {
            result = false;
        }
    }
}