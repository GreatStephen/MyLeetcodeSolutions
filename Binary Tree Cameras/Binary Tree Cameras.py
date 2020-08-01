# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # greedy, 叶节点永远不放camera，往叶节点的父节点放。
        # camera能提高就提高。如果子节点被cover但不是camera，当前节点也不放camera，把camera提高
        self.ans = 0
        if not root.left and not root.right: return 1
        def DFS(node): # 0=not covered, 1=covered & no camera, 2=is camera
            # is_camera = False
            if not node.left and not node.right: return 0 # leaf node
            l, r = None, None
            if node.left: l = DFS(node.left)
            if node.right: r = DFS(node.right)
            if l==0 or r==0:
                self.ans += 1
                return 2
            elif l==2 or r==2:
                return 1
            else:
                if node!=root: return 0
                else: self.ans+=1 # root node has no parent, must add a camera here
            
        DFS(root)
        return self.ans