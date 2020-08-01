# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        deq = collections.deque()
        deq.append((root,0))
        d = collections.defaultdict(list)
        self.lo = self.hi = 0
        while len(deq)>0:
            N = len(deq)
            dd = collections.defaultdict(list)
            for _ in range(N):                
                node, idx = deq.popleft()
                self.lo = min(self.lo, idx)
                self.hi = max(self.hi, idx)
                l = dd[idx] or None
                if not l: dd[idx].append(node.val)
                else: l.insert(bisect.bisect_left(l, node.val), node.val)
                if node.left: deq.append((node.left, idx-1))
                if node.right: deq.append((node.right, idx+1))
            # Combine dd into d
            for k,v in dd.items():                
                d[k]+=v     
        
        ans =[d[i] for i in range(self.lo, self.hi+1)]
        return ans