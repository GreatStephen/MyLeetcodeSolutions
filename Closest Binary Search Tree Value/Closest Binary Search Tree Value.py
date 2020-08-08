# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        diff = float('inf')
        ans = None
        
        cur = root
        while cur:
            if abs(cur.val-target)<diff:
                ans = cur.val
                diff = abs(cur.val-target)
            if cur.val<target:
                cur = cur.right
            else:
                cur = cur.left
                
        return ans