# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # key: among root.left and root.right there will always be a full tree
        def height(root, direc):    # 0->left, 1->right
            ans = 0
            while root:
                ans+=1
                if direc==0: root = root.left
                elif direc==1: root = root.right
            return ans
        
        def helper(root):
            if not root: return 0
            hl, hr = height(root, 0), height(root, 1)
            if hl==hr: return (2**hl)-1
            else: return 1+helper(root.left)+helper(root.right)
        
        return helper(root)
            