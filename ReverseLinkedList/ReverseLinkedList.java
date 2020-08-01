/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head==null) return null;
        ListNode fakehead = new ListNode(-1);
        fakehead.next = head;
        head = head.next;
        fakehead.next.next = null;
        while(head!=null){
            ListNode headnext = head.next;
            head.next=fakehead.next;
            fakehead.next=head;
            head=headnext;
        }
        return fakehead.next;
    }
}