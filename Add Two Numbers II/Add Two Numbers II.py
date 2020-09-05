# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 用stack存储所有的数字。
        s1, s2 = deque(), deque()
        cur = l1
        while cur:
            s1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            s2.append(cur.val)
            cur = cur.next
        
        carry = 0
        head, temp = None, None
        while s1 and s2: # 倒序加两个stack
            val = s1[-1]+s2[-1]+carry
            carry = val//10
            val %= 10
            head = ListNode(val, temp)
            temp = head
            s1.pop()
            s2.pop()
        
        s = s1 if s1 else s2
        while s: # 如果剩了某一个stack，就把它加进去
            val = s[-1]+carry
            carry = val//10
            val %= 10
            head = ListNode(val, temp)
            temp = head
            s.pop()
        if carry:
            head = ListNode(1, temp)
            temp = head
        return temp
        
        