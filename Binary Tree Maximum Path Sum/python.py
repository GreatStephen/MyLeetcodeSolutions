
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 任何tree的问题，都可以用pre/in/post order遍历来解决。这道题是后序遍历。
        # 遍历左，右，然后加上自己（自己是必加的，因为题目要求path长度不能为0）
        # 返回给上一层的max有可能<0，这时候需要父节点自己取max(,0)即可
        self.ans = float('-inf')
        def traverse(node):
            if not node: return 0
            left = max(traverse(node.left), 0)
            right = max(traverse(node.right), 0)
            self.ans = max(self.ans, left + right + node.val)
            return max(left, right)+node.val
        
        traverse(root)
        return self.ans