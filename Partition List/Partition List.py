# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 类似于quicksort的算法，原地更改node顺序
        if not head: return None
        dummy = ListNode(next = head)
        l = r = dummy
        while r.next.val<x:
            r = r.next
            if not r.next: break
        while r.next:            
            # l.next finds the first >=x node
            while l.next.val<x: l = l.next
            # r.next finds the first <x node            
            while r.next.val>=x:
                r = r.next    
                if not r.next: break
            if not r.next: break
            ln, rn = l.next, r.next
            r.next = rn.next
            rn.next = ln
            l.next = rn
        return dummy.next