
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        # 漂亮的代码
        # 用递归的方法找到root=key，小于就使root.left=左递归，大于就root.right=右递归
        # 如果找到root=key，如果left为空，返回右，如果right为空，返回左。这时如果两边都为空，返回值也一定是空
        # 如果root有两个子树，找到右子树的最小值，然后让root=minval，然后对右子树递归删除这个minval
        if not root:
            return None
        if key<root.val:
            root.left = self.deleteNode(root.left, key)
        elif key>root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)        
        
        return root

