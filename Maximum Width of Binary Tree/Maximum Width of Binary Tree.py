# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.left, self.right = [1], [1]
        self.ans = 0
        def DFS(node, level, idx):
            if level>=len(self.left): self.left.append(idx)
            else: self.left[level] = min(self.left[level], idx)
            if level>=len(self.right): self.right.append(idx)
            else: self.right[level] = max(self.right[level], idx)
            self.ans = max(self.ans, self.right[level]-self.left[level]+1)
            if node.left: DFS(node.left, level+1, idx*2)
            if node.right: DFS(node.right, level+1, idx*2+1)
        DFS(root, 0, 1)
        return self.ans