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
        return DFS(root, 1);
    }

    private int DFS(TreeNode node, int cur_depth){
        if(node==null){
            return cur_depth-1;
        }

        int res = 0;
        int left_depth = DFS(node.left, cur_depth+1);
        res = Math.max(res, left_depth);
        int right_depth = DFS(node.right, cur_depth+1);
        res = Math.max(res, right_depth);

        return res;
    }
}