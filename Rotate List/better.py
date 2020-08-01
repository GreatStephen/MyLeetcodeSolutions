# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        tail, count = head, 1
        while tail.next:            
            tail = tail.next
            count += 1
        if k==count: return head
        k = count - (k%count)   # move left by k steps now
        
        n = head
        for _ in range(1, k):
            n = n.next  # find the kth node from the left
        tail.next = head
        head = n.next
        n.next = None
        return head