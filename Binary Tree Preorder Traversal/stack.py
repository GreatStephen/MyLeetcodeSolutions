# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        deq, n, ans = deque(), root, []
        while n:
            if n.right: deq.append(n.right)
            ans.append(n.val)
            n = n.left
            if not n and deq: n = deq.pop()               
        return ans