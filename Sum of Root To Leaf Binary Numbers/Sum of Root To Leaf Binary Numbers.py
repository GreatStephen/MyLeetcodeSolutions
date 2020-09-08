# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        # 简单的DFS
        def DFS(cur, parent):
            if not cur.left and not cur.right:
                return [[cur.val]]
            arr = []
            if cur.left:
                arr+=DFS(cur.left, cur)
            if cur.right:
                arr+=DFS(cur.right, cur)
            for i in range(len(arr)):
                arr[i].insert(0, cur.val)
            return arr
        
        arr = DFS(root, None)
        ans = 0
        for a in arr:
            temp = ''.join(str(a[i]) for i in range(len(a))) # 将二进制数字转成字符串            
            ans += int(temp, 2) # 再转换十进制
        return ans