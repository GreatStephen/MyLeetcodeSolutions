# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # 用stack方法解决这个问题，有够难想
        d = collections.deque()
        for i,v in enumerate(nums):
            cur = TreeNode(v)
            while len(d) and d[-1].val<v: cur.left = d.pop()
            if len(d): d[-1].right = cur
            d.append(cur)
        if len(d): return d[0]
        else: return None