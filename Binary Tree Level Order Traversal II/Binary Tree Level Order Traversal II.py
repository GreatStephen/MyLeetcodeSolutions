# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        deq = collections.deque()
        # level = 0
        deq.append(root)
        ans = []
        while len(deq)!=0:
            N = len(deq)
            nodes = []
            for i in range(N):
                node = deq.popleft()
                nodes.append(node.val)
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
            ans.insert(0,nodes)
        return ans