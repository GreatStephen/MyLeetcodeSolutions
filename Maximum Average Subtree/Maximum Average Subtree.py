# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        # 简单的DFS。每个节点返回给parent自己的[总数，个数]
        self.ans = 0
        def DFS(cur):
            if not cur: return (0,0)
            if not cur.left and not cur.right:
                self.ans = max(self.ans, cur.val)
                return (cur.val, 1)
            left, right = DFS(cur.left), DFS(cur.right)
            temp = (left[0]+right[0]+cur.val, left[1]+right[1]+1)
            self.ans = max(self.ans, temp[0]/float(temp[1]))
            return temp
        
        DFS(root)
        return self.ans