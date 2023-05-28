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
    // approach 1: recursive DFS
    /*
    public int maxDepth(TreeNode root) {
        return DFS(root);
    }
    
    public int DFS(TreeNode node) {
        if (node == null) {
            return 0;
        }
        
        return 1 + Math.max(DFS(node.left), DFS(node.right));
    }
    */
    
    // approach 2: BFS
    
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int level = 0;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.remove();
                
                if (node.left != null) {
                    queue.add(node.left);
                }
                
                if (node.right != null) {
                    queue.add(node.right);
                }
            }
            
            level++;
        }
        
        return level;
    }
}