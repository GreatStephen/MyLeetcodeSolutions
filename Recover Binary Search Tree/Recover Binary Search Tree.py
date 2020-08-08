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
        # Morris Traversal
        # 这道题的要点除了Morris，还有prev.val>cur.val是异常，第一次出现的位置必定是原tree中较小的那个节点
        # 所以第一次出现时，prev的位置必定是abnormal。edge case: 如果两个异常节点是父子关系，那么这时cur是第二个，所以暂时把cur赋值给second
        # 如果第二次出现prev>cur，这时cur是第二个异常
        self.first = None
        self.second = None
        self.prev = None
        
        cur = root
        while cur:
            if cur.left:
                # left subtree exists, build connection or break connection
                temp = cur.left
                while temp.right and temp.right!=cur:
                    temp = temp.right
                if temp.right:
                    # break the connection
                    temp.right = None
                    if self.prev and self.prev.val>cur.val:
                        if not self.first: self.first = self.prev
                        self.second = cur
                    self.prev = cur
                    cur = cur.right
                else:
                    temp.right = cur
                    cur = cur.left
            
            else:
                # no left subtree, start to compare
                if self.prev and self.prev.val>cur.val:
                    if not self.first: self.first = self.prev
                    self.second = cur
                self.prev = cur
                cur = cur.right
        
        self.first.val, self.second.val = self.second.val, self.first.val