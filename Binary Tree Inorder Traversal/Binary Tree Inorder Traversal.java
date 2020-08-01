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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        TreeNode cur = root;
        while(cur!=null){
            System.out.println(cur.val);
            if(cur.left == null){
                res.add(cur.val);
                cur = cur.right;
            }
            else{
                TreeNode cur_left = cur.left;
                TreeNode cur_left_rightmost = cur_left;
                while(cur_left_rightmost.right!=null){
                    cur_left_rightmost = cur_left_rightmost.right;
                }
                cur_left_rightmost.right = cur;
                cur.left = null;
                cur = cur_left;
            }
        }
        return res;
    }
}