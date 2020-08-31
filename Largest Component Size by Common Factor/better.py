class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        d = {} # a factor contains a set, store the root element from this set
        group = {}
        
        def find(x): # find and uniformize
            if x != group[x]:
                group[x] = find(group[x])
            return group[x]
        
        def unionGroup(x,y): # union the root of y to the root of x
            if x not in group: group[x] = x
            if y not in group: group[y] = y
            g1, g2 = find(x), find(y)
            if g1!=g2:
                group[g2] = g1 # [g1]=g2 the same
            
        for num in A:
            if num==1: # 1要特殊处理，1必须自己一个组
                group[num] = num
                continue
            for x in range(2, int(math.sqrt(num))+1): # x是可能的因数
                if num%x==0:
                    if x not in d:
                        d[x] = num
                    else: # 这个因数已经出现过，就把当前数字的组归并到这个因数所在的组
                        unionGroup(d[x], num)
                    if num/x not in d:
                        d[num/x] = num
                    else: # 如果x是因数，num/x也是因数
                        unionGroup(d[num/x], num)
            if num not in d: # num自己也是个因数，不要忘了
                d[num] = num
            else:
                unionGroup(d[num], num)
                        
        ans = {}
        for num in group: # 统计每个组有多少个组员
            g = find(num)
            if g not in ans:
                ans[g] = 0
            ans[g] += 1
        
        return max(ans.values())
                
            