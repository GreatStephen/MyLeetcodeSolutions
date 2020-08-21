class Solution(object):
    def minimumDistance(self, word):
        # 自己做出来的hard DP。三维DP，保存当前两个字符分别是什么，以及当前是第k个字符
        # 移动f1的距离+下一个dp， 和移动f2的距离+下一个dp，两者取最小值即可
        def dist(c1, c2): # 计算两个字符的曼哈顿距离
            if c1=='$' or c2=='$':
                return 0
            num1, num2 = ord(c1)-65, ord(c2)-65
            i1, j1 = num1/6, num1%6
            i2, j2 = num2/6, num2%6
            return abs(i1-i2)+abs(j1-j2)
        
        d = {}        
        def DP(f1, f2, k): # 保存三个维度
            if k>=len(word):
                return 0
            if (f1, f2, k) in d:
                return d[(f1, f2, k)]
            c = word[k]
            ans = min(dist(f1,c)+DP(c,f2,k+1), dist(f2,c)+DP(f1,c,k+1))
            d[(f1, f2, k)] = ans
            return ans
            
    
        return DP('$', '$', 0)