# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        
        q = deque()
        
        level = 0
        q.append(root)
        
        while q:
            next_level = []
            val = 10**7 if level&1 else 0
            while q:
                cur = q.popleft()
                if not level&1:
                    if not cur.val&1 or cur.val<=val:
                        return False
                if level&1:
                    if cur.val&1 or cur.val>=val:
                        return False
                val = cur.val
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
            q.extend(next_level)
            level += 1
        
        return True
                    