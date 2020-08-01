# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def helper(nodes: List[int])->List[TreeNode]:
            if len(nodes)==0: return None
            if len(nodes)==1: return list([TreeNode(nodes[0])])
            ans = []
            for i,n in enumerate(nodes):
                left = helper(nodes[:i]) or [None]
                right = helper(nodes[i+1:]) or [None]
                for head_l in left:
                    for head_r in right:
                        ans.append(TreeNode(n, left=head_l, right=head_r))
            return ans

        ans = helper([i for i in range(1, n+1)])
        return ans