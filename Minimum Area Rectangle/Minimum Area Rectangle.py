class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # 记录每个x对应的所有y，遍历x，对每一个x，找到所有的y pairs，检查这个ypair是否曾经出现过
        # 如果出现过，说明可以和之前的某个x组成矩形。没出现过就放进dict继续
        # 优化：x选择多的一边，y选择少的一边，因为x是线性时间，y是n^2时间
        d = collections.defaultdict(list)
        for p in points:
            d[p[0]].append(p[1])
        
        r = collections.defaultdict(int)
        ans = 10**9
        for x in sorted(d):
            for i in range(len(d[x])):
                for j in range(i+1, len(d[x])):
                    yp = (d[x][i], d[x][j])
                    yp_r = (d[x][j], d[x][i])
                    if yp in r:
                        ans = min(ans, (x-r[yp])*abs(yp[0]-yp[1]))
                    r[yp], r[yp_r] = x, x                    
        
        return ans if ans<10**9 else 0