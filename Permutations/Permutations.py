class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for n in nums:
            if len(ans)==0: 
                ans.append([n])
                continue
            N = len(ans)
            for i in range(N):
                l = ans.pop(0)
                for j in range(len(l)+1):
                    new_l = list(l) # 这里效率太低了，先hardcopy再insert很慢，应该直接拼接list
                    new_l.insert(j,n)
                    ans.append(new_l)
        
        if len(ans)==0: return [[]]
        return ans
