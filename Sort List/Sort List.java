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
    public ListNode sortList(ListNode head) {
        // this is quictsort in linkedlist
        // mergesort is better
        if(head==null){
            return null;
        }
        if(head.next == null){
            return head;
        }
        ListNode pivot = head;
        ListNode point = head.next;
        pivot.next = null;
        // dummy heads
        ListNode less_head = new ListNode();
        ListNode less_point = less_head;
        ListNode larger_head = new ListNode();
        ListNode larger_point = larger_head;

        while(point!=null){
            if(point.val>=pivot.val){
                larger_point.next = point;
                larger_point = larger_point.next;
                point = point.next;
                larger_point.next = null;
            }
            else{
                less_point.next = point;
                less_point = less_point.next;
                point = point.next;
                less_point.next = null;
            }
            
        }

        // System.out.println(less_head.val);
        // System.out.println(larger_head.val);

        less_head = sortList(less_head.next);
        larger_head = sortList(larger_head.next);

        pivot.next = larger_head;
        if(less_head==null){
            return pivot;
        }

        ListNode less_tail = less_head;
        while(less_tail.next!=null){
            less_tail = less_tail.next;
        }

        less_tail.next = pivot;

        return less_head;

    }
}