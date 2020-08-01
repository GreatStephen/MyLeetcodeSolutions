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
    public int kthSmallest(TreeNode root, int k) {
        // very nice iteration in-order traversal
        // the stack is a descending array
        LinkedList<TreeNode> linkedlist = new LinkedList();
        while(true){
            while(root!=null){
                linkedlist.push(root);
                root = root.left;
            }
            if(linkedlist.isEmpty()){
                break;
            }
            root = linkedlist.pop();
            if(--k==0){
                return root.val;
            }
            root = root.right;
        }

        return -1;
    }
}