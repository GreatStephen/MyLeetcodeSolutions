class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # 直接使用滑窗。找到包含k个unique字符的最短子串，然后移动l，剔除所有重复出现过的字符，那么prefix的长度即为当前有效的结果
        # 每次向右移动r一位，就重复上一步。但如果发现r位字符不包括在当前窗口中，prefix需要清零，因为l是不能往前扩展的
        l, r, seen, d = 0, 0, set(), {}
        ans, prefix = 0, 0
        while r<len(A):
            if A[r] not in d:
                d[A[r]] = 1
                K -= 1                
            else:
                d[A[r]] += 1
            r += 1
            if K>0: continue
            
            # K+1 unique elements, move l until K left
            while K<0:
                if d[A[l]] ==1:
                    del d[A[l]]
                    K+=1
                    prefix = 0
                elif d[A[l]] >1:
                    d[A[l]] -=1
                l += 1                
            
            # K unique elements, move l right
            if K==0:
                while d[A[l]]>1:
                    d[A[l]]-=1
                    l+=1
                    prefix+=1
                ans += prefix+1
                
        return ans