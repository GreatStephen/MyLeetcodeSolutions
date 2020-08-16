class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        length = k**n-1+n       
        
        # DFS。把prev提取出来，对所有能衔接的数字做DFS，只要找到一个完整的串，直接返回
        seen = set([''.join([str(0)]*n)])
        def DFS(cur):
            if len(seen)==k**n:
                return cur
            prev = cur[1-n:] if n>1 else ''
            for i in xrange(k): # 对prev尝试加上每一个数字
                nextpwd = prev+str(i)
                if nextpwd in seen:
                    continue
                seen.add(nextpwd)
                ans = DFS((cur[:1-n] if n>1 else cur)+nextpwd)
                if len(ans)>0:
                    return ans
                seen.remove(nextpwd)
            return ''
        
        return DFS(''.join([str(0)]*n))