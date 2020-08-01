
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

 // the value of treenodes may be duplicated!
class Solution {
    Queue<TreeNode> queue;
    public boolean isSubtree(TreeNode s, TreeNode t) {
        queue = new LinkedList<>();
        queue.add(s);
        TreeNode start = BFS(t.val);
        if(start == null) return false;
        if(preOrderTrav(start, "").compareTo(preOrderTrav(t, "")) == 0) return true;
        else return false;

    }

    private TreeNode BFS(int target){
        while(!queue.isEmpty()){
            TreeNode temp = queue.poll();
            if(temp.val == target) return temp;
            if(temp.left!=null) queue.add(temp.left);
            if(temp.right!=null) queue.add(temp.right);
        }
        return null;
    }

    private String preOrderTrav(TreeNode node, String s){
        s+=String.valueOf(node.val);
        if(node.left!=null) s = preOrderTrav(node.left, s);
        if(node.right!=null) s = preOrderTrav(node.right, s);
        return s;
    }
}