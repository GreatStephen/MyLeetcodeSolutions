# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next: return head
        o,e = head, head.next
        while e and e.next:
            n = e.next
            e.next = n.next
            n.next = o.next
            o.next = n
            o = o.next
            e = e.next
        return head