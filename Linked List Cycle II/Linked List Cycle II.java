/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        //phase 1
        ListNode fast=head, slow=head;
        do{
            if(fast==null || fast.next==null) return null;
            fast = fast.next.next;
            slow = slow.next;
        }while(fast!=slow);

        slow=head;
        while(slow!=fast){
            fast = fast.next;
            slow = slow.next;
        }
        return fast;
    }
}