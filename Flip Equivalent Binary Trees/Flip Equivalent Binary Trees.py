# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        # 这题就很简单了，就两种情况，（左=左）+（右=右），或者（左=右）+（右=左），直接递归
        def helper(node1, node2):
            if not node1 and not node2: return True
            if (node1 and not node2) or (node2 and not node1): return False
            if not node1.val==node2.val:
                return False
            if helper(node1.left, node2.left) and helper(node1.right, node2.right): return True
            if helper(node1.left, node2.right) and helper(node1.right, node2.left): return True
            return False
        
        
        return helper(root1, root2)