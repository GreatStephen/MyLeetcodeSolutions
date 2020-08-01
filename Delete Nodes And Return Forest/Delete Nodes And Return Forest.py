# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # Lee215说，用递归处理tree问题
        ans = []
        d = set(to_delete)
        def helper(node, isRoot):
            if node.val not in d and isRoot: ans.append(node)
            if node.left: node.left = helper(node.left, node.val in d)
            if node.right: node.right = helper(node.right, node.val in d)
            if node.val in d:
                return None
            else:
                return node
        helper(root, True)
        return ans