# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        ans = []
        def DFS(node, cur): # cur[0]记录当前路径的sum，[1:]里面是当前路径的所有节点
            cur[0]+=node.val
            cur.append(node.val)
            if not node.left and not node.right:
                if cur[0] == sum:
                    ans.append(cur[1:])
            if node.left:
                DFS(node.left, list(cur))
            if node.right:
                DFS(node.right, list(cur))
            
            
        DFS(root, [0])
        return ans