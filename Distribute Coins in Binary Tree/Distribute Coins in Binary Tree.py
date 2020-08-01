# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        def DFS(node):
            left, right = 0, 0
            if not node.left and not node.right: return node.val-1
            if node.left: left = DFS(node.left)
            if node.right: right = DFS(node.right)
            self.ans += abs(left)+abs(right)
            return node.val+left+right-1
        DFS(root)
        return self.ans