# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 又是一个tree框架题。只需要中序遍历即可。
        # 过程中会出现1次（两个相邻元素交换）或2次（两个不相邻的元素交换）cur<prev的情况
        # 第一次把target1=prev, target2=cur。如果第二次出现，就把target2=cur。最后交换t1,t2的值即可。
        self.prev = None
        self.target1, self.target2 = None, None
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            if self.prev and node.val<self.prev.val:
                if not self.target1:
                    self.target1 = self.prev
                    self.target2 = node
                else:
                    self.target2 = node
            self.prev = node
            traverse(node.right)


        traverse(root)
        self.target1.val, self.target2.val = self.target2.val, self.target1.val
        return 