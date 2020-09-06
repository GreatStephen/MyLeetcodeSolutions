# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # inorder得到两个sorted数组，然后进行merge
        def inOrder(cur, path):
            if not cur: return path
            path = inOrder(cur.left, path)
            path.append(cur.val)
            path = inOrder(cur.right, path)
            return path
        
        def merge(p1, p2):
            idx1, idx2 = 0, 0
            ans = []
            while idx1<len(p1) or idx2<len(p2):
                num1 = p1[idx1] if idx1<len(p1) else float('inf')
                num2 = p2[idx2] if idx2<len(p2) else float('inf')
                if num1<num2:
                    ans.append(num1)
                    idx1 += 1
                elif num2<num1:
                    ans.append(num2)
                    idx2 += 1
                else:
                    ans.append(num1)
                    ans.append(num2)
                    idx1 += 1
                    idx2 += 1
            return ans
        
        p1, p2 = inOrder(root1, []), inOrder(root2, [])
        return merge(p1, p2)