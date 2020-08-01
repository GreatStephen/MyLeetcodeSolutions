/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if(k==1) return head;
        int count=0;
        ListNode countnum=head;
        while(countnum!=null){
            count++;
            countnum=countnum.next;
        }
        if(count<k) return head;

        ListNode fakehead = new ListNode(-1);
        ListNode cur = head;
        fakehead.next = cur;
        cur = cur.next;
        ListNode tail = fakehead.next;
        tail.next=null;

        for(int i=2; i<=k; i++){
            ListNode curnext = cur.next;
            cur.next=fakehead.next;
            fakehead.next=cur;
            cur=curnext;
        }

        tail.next=reverseKGroup(cur, k);

        return fakehead.next;
        
    }
}