# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        d = {}
        for i,n in enumerate(inorder):
            d[n] = i
        # print(d)
        
        def traverse(pl, pr, il, ir):
            # 本质上还是个前序遍历！pre的第一个元素一定是root，然后根据root在in里的位置，划分为左和右
            # 对左和右分别递归，所以是前序遍历
            if pl>pr or il>ir:
                return None
            root = TreeNode(val=preorder[pl])
            idx = d[preorder[pl]]
            llen, rlen = idx-il, ir-idx
            root.left = traverse(pl+1, pl+llen, il, idx-1)
            root.right = traverse(pl+1+llen, pr, idx+1, ir)
            return root
        
        
        root = traverse(0, len(preorder)-1, 0, len(inorder)-1)
        return root