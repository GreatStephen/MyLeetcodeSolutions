class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # 把“额外信息”添加到dp中，即每个数字前面有k个相同数字
        # 存在两种情况，1.当前字符单独拿出来，取得(k+1)2，剩下的继续dp
        # 2.当前字符不动，找到下一个相同字符，两个字符中间的部分dp，当前字符作为(k+1)传递到下一个相同字符处，再继续
        # 两种情况取最大值
        N = len(boxes)
        dp = [[[0]*N for i in range(N) ] for j in range(N)]
        
        def helper(l, r, k):
            if l>r: return 0
            if l==r: return (k+1)*(k+1)
            if dp[l][r][k]!=0: return dp[l][r][k]
            ans = (k+1)*(k+1)+helper(l+1, r, 0)
            
            for m in range(l+1, r+1):
                if boxes[l]==boxes[m]:
                    ans = max(ans, helper(l+1, m-1, 0)+helper(m,r,k+1))
            
            dp[l][r][k]=ans
            return ans
        
        return helper(0, N-1, 0)