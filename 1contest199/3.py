# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # DFS
        self.ans = 0
        
        def DFS(node):
            dl, dr = {}, {}
            dleft, dright = None, None
            if node.left: dleft = DFS(node.left)
            if node.right: dright = DFS(node.right)
            
            # result from left and right subtree
            if dleft:
                for n in dleft.keys(): 
                    dleft[n]+=1
                    dl = dleft
            else:
                if node.left: dl[node.left]=1
            if dright:
                for n in dright.keys(): 
                    dright[n]+=1
                    dr = dright
            else:
                if node.right: dr[node.right]=1
            
            # find answers
            for ldis in dl.keys():
                for rdis in dr.keys():
                    if dl[ldis]+dr[rdis]<=distance: self.ans+=1
            
            # if node.val==7: print(dl, dr)
            # conbime dl and dr, return to parent
            # return dict(dl.items()+dr.items())
            return {**dl, **dr}
        
        
        DFS(root)
        return self.ans
        