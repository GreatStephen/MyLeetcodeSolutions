# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def helper(head, tail):
            if head==tail: return None
            slow, fast = head, head
            while fast.next!=tail and fast.next.next!=tail:
                fast = fast.next.next
                slow = slow.next
            head = TreeNode(slow.val, left=helper(head,slow), right=helper(slow.next, tail))
            return head        
        return helper(head, None)
            