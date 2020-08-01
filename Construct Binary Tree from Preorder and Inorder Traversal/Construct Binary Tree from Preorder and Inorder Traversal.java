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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if(preorder.length==0 && inorder.length==0) return null;
        int pre_index = 0;
        while(preorder[pre_index]!=inorder[0]) pre_index++;
        int sub_index = pre_index+1;

        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<inorder.length; i++){
            map.put(inorder[i], i);
        }

        int in_index=0;
        TreeNode cur_root=null;
        while(pre_index>=0){
            TreeNode root = new TreeNode(inorder[in_index++]);
            int[] sub_preorder = new int[1];
            int[] sub_inorder = new int[1];
            int l = 0;
            if(pre_index==0){
                l = preorder.length-sub_index;
                sub_preorder = new int[l];
                sub_inorder = new int[l];
            }
            else{
                l = map.get(preorder[pre_index-1]) - map.get(preorder[pre_index]) - 1;
                sub_preorder = new int[l];
                sub_inorder = new int[l];
            }
            for(int i=0; i<l; i++){
                sub_preorder[i] = preorder[sub_index++];
                sub_inorder[i] = inorder[in_index++];
            }
            pre_index--;

            root.left = cur_root;
            root.right = buildTree(sub_preorder, sub_inorder);
            cur_root = root;
        }

        return cur_root;
    }
}