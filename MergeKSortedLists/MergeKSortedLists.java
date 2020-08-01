/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length==0) return null;
        if(lists.length==1) return lists[0];

        ListNode head=lists[0];
        for(int i=1; i<=lists.length-1; i++){
            head = mergeTwoLists(head, lists[i]);
        }
        return head;
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode fakehead = new ListNode(-1);
        ListNode tail = fakehead;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }
        if (l1 == null)
            tail.next = l2;
        if (l2 == null)
            tail.next = l1;
        return fakehead.next;
    }
}