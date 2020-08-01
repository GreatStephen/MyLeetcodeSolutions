# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return None
        prev, new_head = head, head
        while prev and prev.val==val:
            prev = prev.next
            new_head = prev
        
        if not prev: return None
        cur = prev.next
        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = prev.next
                cur = cur.next
        return new_head