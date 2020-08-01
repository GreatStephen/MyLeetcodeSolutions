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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if(inorder.length==0 && postorder.length==0) return null;
        ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
        int post_end = postorder.length-1;
        int in_start = 0;
        int in_length = inorder.length;

        while(in_start<in_length){
            ArrayList<Integer> subtree = new ArrayList<>();
            do{
                subtree.add(inorder[in_start]);
            }while(inorder[in_start++] != postorder[post_end]);
            list.add(subtree);
            post_end--;
        }

        // System.out.println(list);
        int post_start = 0;
        in_start = 0;
        ArrayList<TreeNode> rootlist = new ArrayList<TreeNode>();
        for(ArrayList<Integer> item : list){
            TreeNode root = new TreeNode(item.get(item.size()-1));
            int sub_length = item.size()-1;
            int[] sub_inorder = new int[sub_length];
            int[] sub_postorder = new int[sub_length];
            for(int i=0; i<sub_length; i++){
                sub_inorder[i] = inorder[in_start++];
                sub_postorder[i] = postorder[post_start++];
            }
            // to skip the root itself
            in_start++;

            TreeNode left = buildTree(sub_inorder, sub_postorder);
            root.left = left;
            rootlist.add(root);
        }

        // System.out.println(rootlist);
        int i;
        for(i=0; i<rootlist.size()-1; i++){
            rootlist.get(i).right = rootlist.get(i+1);
        }
        rootlist.get(i).right = null;
        return rootlist.get(0);
    }
}