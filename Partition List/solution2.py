# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 分别把nodes存放进两个新链表，稍微快一些
        l, ge = ListNode(),ListNode()
        n, l_tail, ge_tail = head, l, ge
        while n:
            if n.val<x:
                l_tail.next = n
                l_tail = l_tail.next
            else:
                ge_tail.next = n
                ge_tail = ge_tail.next
            n = n.next
        l_tail.next, ge_tail.next = None, None
        if not l.next: return ge.next
        if not ge.next: return l.next
        l_tail.next = ge.next
        return l.next