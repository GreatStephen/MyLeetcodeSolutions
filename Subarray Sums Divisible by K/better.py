class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # 还是O(N)时间，少了两次遍历，只需要一次遍历
        # 技巧：当字典宽度固定时，可以用list代替dict，节省一些时间
        ans = 0
        l = [1]+[0]*(K-1)
        prefix = 0
        for a in A:
            prefix = (prefix+a)%K
            ans += l[prefix]
            l[prefix] +=1
        
        return ans