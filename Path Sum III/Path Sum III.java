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
    public int pathSum(TreeNode root, int sum) {
        if(root == null){
            return 0;
        }
        int res=-1;
        res = DFS(root, sum, 0, 0) + pathSum(root.left, sum) + pathSum(root.right, sum);
        
        return res;
    }

    private int DFS(TreeNode node, int sum, int tempres, int tempsum){
        if(node == null){
            return tempres;
        }
        if(node.val+tempsum == sum){
            tempres++;
        }
        tempsum+=node.val;

        tempres = DFS(node.left, sum, tempres, tempsum);
        tempres = DFS(node.right, sum, tempres, tempsum);
        
        return tempres;
    }
}