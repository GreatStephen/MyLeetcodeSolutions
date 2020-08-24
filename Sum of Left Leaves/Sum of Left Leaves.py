# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        # 递归，加上一个参数，当前节点是否来自父亲的左子树。
        # 如果当前是leaf，且来自父亲的左子树，就加到ans里
        self.ans = 0
        def helper(node, left):
            if not node:
                return 0
            if not node.left and not node.right and left:
                self.ans += node.val
                return
            if node.left:
                helper(node.left, True)
            if node.right:
                helper(node.right, False)
            return
        
        
        
        helper(root, None)
        return self.ans