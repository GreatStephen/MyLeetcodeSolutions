/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        // cur <= p, go left
        // cur > p, go right, until reach null
        TreeNode cur = root;
        TreeNode ans = null;
        while(cur!=null){
            if(cur.val<=p.val){
                cur = cur.right;
            }
            else{
                ans = cur;
                cur = cur.left;
            }
        }
        return ans;
    }
}