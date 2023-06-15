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
    
    boolean isSameTree = true;
    boolean result = false;
    
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // approach: DFS -> when roots are same, call same tree
        
        dfs(root, subRoot);
        return result;
    }
    
    private void dfs(TreeNode root, TreeNode subRoot) {
        if (root == null || subRoot == null) {
            return;
        }
        
        if (root.val == subRoot.val) {
            isSameTree = true;
            helper(root, subRoot);
            
            if (isSameTree) {
                result = true;
            }
        }
        
        dfs(root.left, subRoot);
        dfs(root.right, subRoot);
    }
    
    private void helper(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return;
        }
        
        if (p == null || q == null) {
            isSameTree = false;
            return;
        }
        
        if (p.val != q.val) {
            isSameTree = false;
        }
        
        helper(p.left, q.left);
        helper(p.right, q.right);
    }
}