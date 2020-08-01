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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        // BFS+Queue solution
        // <root.val, level>
        Deque<TreeNode> q = new LinkedList();
        Deque<Integer> flag = new LinkedList();
        List<List<Integer>> ans = new ArrayList();

        // initial node
        if(root!=null){
            q.offerLast(root);
            flag.offerLast(0);
        } 
        else{
            return new ArrayList();
        }
        

        // iteration
        int cur_level = 0;
        List<Integer> temp = new ArrayList();
        while(!q.isEmpty()){
            TreeNode node = q.pollFirst();
            int level = flag.pollFirst();

            if(level!=cur_level){
                // end of a row
                ans.add(temp);
                cur_level = level;
                temp = new ArrayList();
            }
            if(cur_level%2==0) temp.add(node.val);
            else temp.add(0, node.val);

            if(node.left!=null){
                q.offerLast(node.left);
                flag.offerLast(level+1);
            } 
            if(node.right!=null){
                q.offerLast(node.right);
                flag.offerLast(level+1);
            }
        }
        ans.add(temp);

        return ans;
    }
}