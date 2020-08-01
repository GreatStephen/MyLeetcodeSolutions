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
    private int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        max_gain(root);
        return max;
    }

    private int max_gain(TreeNode node){
        if(node==null){
            return 0;
        }
        // let it >=0, because if positive number exists, all the negative numbers can be treated as 0.
        // if positive numbers don't exist, the single root.val is the MAX, and we start from root.
        int left_gain = Math.max(max_gain(node.left),0);
        int right_gain = Math.max(max_gain(node.right),0);

        // max includes both sides
        max = Math.max(max, node.val+left_gain+right_gain);

        // return value includes only on side, because parent node could use only one side.
        return node.val+Math.max(left_gain, right_gain);
    }
}