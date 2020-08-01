/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        // DFS
        String ans = "";
        ans = DFS(root, ans);
        return ans.substring(0, ans.length()-1);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] nodes = data.split(",");
        List<String> list = new ArrayList();
        for(String str: nodes){
            list.add(str);
        }
        TreeNode root = preorder(list);
        return root;
    }

    private String DFS(TreeNode node, String temp_str){
        if(node==null){
            temp_str = temp_str+"null,";
            return temp_str;
        }
        else{
            temp_str = temp_str+String.valueOf(node.val)+",";
            temp_str = DFS(node.left, temp_str);
            temp_str = DFS(node.right, temp_str);
            return temp_str;
        }
    }

    private TreeNode preorder(List<String> list){
        if(!list.get(0).equals("null")){
            TreeNode node = new TreeNode(Integer.valueOf(list.get(0)));
            list.remove(0);
            node.left = preorder(list);
            node.right = preorder(list);
            return node;
        }
        else{
            list.remove(0);
            return null;
        }
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));