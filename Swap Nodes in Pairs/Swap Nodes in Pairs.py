# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next: return head
        new_head = head.next
        a, b, prev = head, head.next, None

        while True:
            a.next = b.next
            b.next = a
            if prev: prev.next = b
                
            a = a.next
            if a: b = a.next
            else: break
            if not b: break
            else: 
                if prev: prev = prev.next.next
                else: 
                    prev = head
        
        return new_head
        