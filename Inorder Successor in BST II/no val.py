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
        # 不比较val值怎么做？
        if node.right:
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur
        else:
            cur = node.parent
            prev = node
            while cur and cur.right==prev: # 很简单，我们只要保证parent.left=prev即可。我们只要右父节点。
                prev = cur
                cur = cur.parent
            return cur