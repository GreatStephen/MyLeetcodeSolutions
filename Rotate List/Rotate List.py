# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        ListNode tail = head
        count = 1
        while tail.next:            
            tail = tail.next
            count += 1
        k %= count
        k = count - k
        
        for _ in range(k):
            tail.next = head
            head = head.next
            tail = tail.next
            tail.next = null
        return head