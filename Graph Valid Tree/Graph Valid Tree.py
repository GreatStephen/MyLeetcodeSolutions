class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # union find是个好东西。把所有的edge做union find，然后检查是否所有的节点都拥有同一个root即可。
        group = [i for i in range(n)]
        
        def find(x):
            if x==group[x]:
                return x
            else:
                group[x] = find(group[x]) # 这是一个技巧，每一次find(x)，都把x直接指向root，这样可以减小level，大幅节省时间
                return group[x]
        
        for s,t in edges:
            root1, root2 = find(s), find(t)
            if root1==root2:
                return False
            else:
                group[root1] = root2
        
        root = find(0) # 所有节点必须拥有同一个root
        for node in range(n):
            if find(node)!=root:
                return False
        return True
            