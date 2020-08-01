/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        // just need O(1) space, very smart solution
        if(root==null) return null;
        root.next = null;
        Node leftmost = root;

        while(leftmost.left!=null){
            Node cur = leftmost;
            Node cur_next = cur.next;
            while(cur_next!=null){
                cur.left.next = cur.right;
                cur.right.next = cur_next.left;
                cur = cur_next;
                cur_next = cur_next.next;
            }
            cur.left.next = cur.right;

            leftmost = leftmost.left;
        }

        return root;
    }
}