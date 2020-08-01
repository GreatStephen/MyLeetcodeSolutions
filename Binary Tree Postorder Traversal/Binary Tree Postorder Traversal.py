# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        deq = deque()
        ans, n = [], root
        while n:
            ans.insert(0, n.val)
            if n.left: deq.append(n.left)
            n = n.right
            if not n and deq: n = deq.pop()
        return ans