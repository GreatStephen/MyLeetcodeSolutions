# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        data = collections.defaultdict(list)
        # build a map of adjacent values
        def recur(parent, child):
            if parent and child:
                data[child.val].append(parent.val)
                data[parent.val].append(child.val)
            if child.left: recur(child, child.left)
            if child.right: recur(child, child.right)
        recur(None, root)
        
        ans = [target.val]
        seen = set([target.val])
        for i in range(K):
            next_level = []
            for node in ans:
                l = data[node]
                for v in l:
                    if v not in seen: next_level.append(v)
            ans = next_level
            seen = seen.union(set(next_level))
        
        return ans