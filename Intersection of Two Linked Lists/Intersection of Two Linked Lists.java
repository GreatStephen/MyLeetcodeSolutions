/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // 2 pointers solution        
        ListNode a = headA, b = headB;
        ListNode lastA = null, lastB = null;

        if(a==null || b==null){
            return null;
        }

        while(a!=b){
            if(a.next==null){
                lastA = a;
                a = headB;
                if(lastA!=null && lastB!=null){
                    if(lastA!=lastB){
                        return null;
                    }
                }
            }
            else{
                a = a.next;
            }
            if(b.next==null){
                lastB = b;
                b = headA;
                if(lastA!=null && lastB!=null){
                    if(lastA!=lastB){
                        return null;
                    }
                }
            }
            else{
                b = b.next;
            }
        }
        return a;
    }
}