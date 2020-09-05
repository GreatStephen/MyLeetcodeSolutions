# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        # 这道题用preorder。因为BST的特性是，左边的一定小于root，右边的一定大于root
        # 所以串行化后的字符串，只需要找到小于root和大于root的分界线，即可递归
        def preOrder(cur):
            if not cur:
                return None
            left, right = preOrder(cur.left), preOrder(cur.right)
            ans = str(cur.val)
            if left: ans += ','+left
            if right: ans += ','+right
            return ans
        
        ans = preOrder(root)
        return ans
        

    def deserialize(self, data: str) -> TreeNode:
        def parse(nodes):
            if not nodes:
                return None
            root = TreeNode(nodes[0])
            left, right = [], []
            idx = -1
            for i in range(1, len(nodes)):
                if nodes[i]<nodes[0]: left.append(nodes[i])
                else: right.append(nodes[i])
            root.left = parse(left)
            root.right = parse(right)
            return root
                
        
        if not data: return None
        nodes = data.split(',')
        nodes = list(map(int, nodes))
        return parse(nodes)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))