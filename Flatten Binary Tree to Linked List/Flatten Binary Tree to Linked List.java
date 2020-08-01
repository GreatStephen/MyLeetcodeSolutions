
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
    public void flatten(TreeNode root) {
        // System.out.println("try");
        if(root==null){
            return;
        }
        TreeNode left_head = root.left;
        TreeNode point = left_head;
        TreeNode right_head = root.right;
        if(left_head!=null){
            flatten(root.left);
            while(point.right!=null){
                point = point.right;
            }
            root.right = left_head;
            root.left = null;
            point.right = right_head;
        }
        
        if(right_head!=null){
            flatten(right_head);            
        }
    }
}