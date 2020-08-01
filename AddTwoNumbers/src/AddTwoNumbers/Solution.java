package AddTwoNumbers;

import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
//        int[] input = new int[4];
        ListNode l11 = new ListNode(0);
        l11.val=scanner.nextInt();
        ListNode l12 = new ListNode(0);
        l12.val=scanner.nextInt();
        ListNode l13 = new ListNode(0);
        l13.val=scanner.nextInt();
        ListNode l21 = new ListNode(0);
        l21.val=scanner.nextInt();
        ListNode l22 = new ListNode(0);
        l22.val=scanner.nextInt();
//        ListNode l23 = new ListNode(0);
//        l23.val=scanner.nextInt();

        l11.next=l12;
        l12.next=l13;
        l21.next=l22;
//        l22.next=l23;

        ListNode res = addTwoNumbers(l11,l21);
        System.out.println(res.val);
        System.out.println(res.next.val);
        System.out.println(res.next.next.val);
//        System.out.println(res.next.next.next.val);
    }
    static public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode p1=l1, p2=l2;
        ListNode head=null;
        ListNode tail=null;
        int carry=0;
        int value=0;

        while(p1!=null || p2!=null){
            ListNode newNode = new ListNode(0);
            if(p1!=null){
                value=(p2!=null)?(p1.val+p2.val+carry)%10:(p1.val+carry)%10;
                carry=(p2!=null)?(p1.val+p2.val+carry)/10:(p1.val+carry)/10;
            }

            else{
                value=(p2.val+carry)%10;
                carry=(p2.val+carry)/10;
            }

//            System.out.println(value);
//            System.out.println(carry);
            newNode.val=value;
            if(head==null){
                head=newNode;
                tail=newNode;
            }
            else{
                tail.next=newNode;
                tail=tail.next;
            }


            if(p1!=null) p1=p1.next;
            if(p2!=null) p2=p2.next;
        }
        if(carry==1){
            ListNode newNode = new ListNode(0);
            newNode.val=1;
            tail.next=newNode;
            tail=tail.next;
        }

        return head;

    }
    static public class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
     }
}
