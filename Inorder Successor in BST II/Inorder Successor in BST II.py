"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # 两种情况，位于node的右子树的最左端，或者位于node的某一个大于node的parent
        if node.right: # 存在右子树，那么一定在右子树
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur
        else: # 不存在右子树，那么就往上找到第一个val>cur.val的parent
            prev = node
            cur = node.parent
            while cur and cur.val<prev.val:
                prev = cur
                cur = cur.parent
            return cur # 如果找不到合适的，cur会等于None