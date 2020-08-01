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
    // DP solution, use a hashmap
    // if root counts, res=root.val + rob 4 grand_children
    // if root does not count, res = rob(left_child) + rob(right_child)
    HashMap<TreeNode, Integer> map = new HashMap();
    public int rob(TreeNode root) {
        if(root==null){
            return 0;
        }
        if(map.containsKey(root)){
            return map.get(root);
        }

        // root counts
        int left_val = 0, right_val = 0;
        if(root.left!=null){
            left_val = rob(root.left.left)+rob(root.left.right);
        }
        if(root.right!=null){
            right_val = rob(root.right.left)+rob(root.right.right);
        }
        int count_val = root.val+left_val+right_val;

        // root doesn't count
        int not_count_val = rob(root.left)+rob(root.right);

        int res = Math.max(count_val, not_count_val);

        map.put(root, res);

        return res;
    }
}