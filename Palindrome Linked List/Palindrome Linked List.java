
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        // reverse the second half in place
        // very good solution
        
        // make sure at least 2 nodes
        if(head==null){
            return true;
        }
        if(head.next==null){
            return true;
        }

        // find the half index
        ListNode slow = head, fast = head;
        while(fast.next!=null && fast.next.next!=null){
            slow = slow.next;
            fast = fast.next.next;
        }

        // reverse the second half
        ListNode cur = slow;
        ListNode tail = cur.next;
        ListNode p = tail.next;
        while(p!=null){
            tail.next = p.next;
            p.next = cur.next;
            cur.next = p;
            p = tail.next;
        }

        // check if palindrome
        ListNode head2 = cur.next;
        ListNode head1 = head;
        while(head2!=null){
            if(head1.val != head2.val){
                return false;
            }
            head1 = head1.next;
            head2 = head2.next;
        }
        return true;
    }
}