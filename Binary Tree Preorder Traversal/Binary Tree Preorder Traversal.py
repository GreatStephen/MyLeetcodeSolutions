# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 提前判断子节点是否None，速度会快很多，减少递归层级
        ans = [root.val]
        if root.left: ans += self.preorderTraversal(root.left)
        if root.right: ans += self.preorderTraversal(root.right)
        return ans